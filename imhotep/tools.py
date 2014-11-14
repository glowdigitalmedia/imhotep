import logging
from collections import defaultdict


log = logging.getLogger(__name__)


class Tool(object):
    """
    Tool represents a program that runs over source code. It returns a nested
    dictionary structure like:

      {'relative_filename': {'line_number': [error1, error2]}}
      eg: {'imhotep/app.py': {'103': ['line too long']}}
    """

    def __init__(self, command_executor, filenames=None, linter=None,
                 config=None, extension=None):
        self.executor = command_executor
        self.filenames = filenames
        self.linter = linter
        # Config file should be in the root folder of the repo
        self.config = config
        self.extension = extension
        if not self.linter and self.extension:
            raise NotImplementedError()

    def get_executor_output(self, command):
        return self.executor(command).split('\n')

    def get_absolute_paths(self, repo_dir, filenames):
        """
        Finds all paths to files with self.extension in the repo dir,
        returns absolute paths to given filenames
        """
        ext_filenames = [
            name for name in filenames if name.endswith(self.extension)
        ]
        find_cmd = 'find {} -name "*.{}"'.format(
            repo_dir,
            self.extension
        )
        all_ext_paths = self.get_executor_output(find_cmd)

        absolute_paths = []
        for path in all_ext_paths:
            if not ext_filenames:
                break
            for filename in ext_filenames:
                if filename in path:
                    absolute_paths.append(path)
                    ext_filenames.remove(filename)
                    break

        return ' '.join(absolute_paths)

    def get_linter_command(self, absolute_paths, config_path=None):
        if config_path:
            command = '{} --config={} {}'.format(
                self.linter, config_path, absolute_paths
            )
        else:
            command = '{} {}'.format(self.linter, absolute_paths)

        return command

    def process_line(self, dirname, line):
        """
        Processes a line return a 3-element tuple representing (filename,
        line_number, error_messages) or None to indicate no error.

        :param: dirname - directory the code is running in
        """

        raise NotImplementedError()

    def format_linter_output(self, repo_dir, linter_output, linter_errors):
        """
        Returns linter errors in the format of:

        {'filename': {
          'line_number': [
            'error1',
            'error2'
            ]
          }
        }
        """

        for line in linter_output:
            output = self.process_line(repo_dir, line)
            if output is not None:
                filename, lineno, messages = output
                if filename.startswith(repo_dir):
                    filename = filename[len(repo_dir) + 1:]
                linter_errors[filename][lineno].append(messages)
        return linter_errors

    def invoke(self, dirname, filenames=None, config_path=None):
        """ Main entrypoint for all plugins. """

        linter_errors = defaultdict(lambda: defaultdict(list))

        if filenames:
            absolute_paths = self.get_absolute_paths(dirname, filenames)
            command = self.get_linter_command(absolute_paths, config_path)
            output = self.get_executor_output(command)
            linter_errors = self.format_linter_output(
                dirname, output, linter_errors
            )
        else:
            log.warning(
                'No files to lint.', RuntimeWarning
            )

        return linter_errors
