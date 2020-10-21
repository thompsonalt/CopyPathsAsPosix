from fman import DirectoryPaneCommand, show_alert, clipboard, show_status_message
from fman.url import as_human_readable
from pathlib import Path

class CopyPathsAsPosix(DirectoryPaneCommand):
	def __call__(self):
		to_copy = self.get_chosen_files() or [self.pane.get_path()]
		files = '\n'.join(to_copy)
		clipboard.clear()
		for path in map(as_human_readable, to_copy):
			posix_path = Path(path).as_posix()
		clipboard.set_text('\n'.join([Path(path).as_posix() for path in map(as_human_readable, to_copy)]))
		# clipboard.set_text('\n'.join(map(as_human_readable, to_copy)))
		_report_clipboard_action('Copied', to_copy, ' to the clipboard as posix paths', 'path')


def _report_clipboard_action(verb, files, suffix='', ftype='file'):
	num = len(files)
	first_file = as_human_readable(files[0])
	if num == 1:
		message = '%s %s%s' % (verb, first_file, suffix)
	else:
		plural = 's' if num > 2 else ''
		message = '%s %s and %d other %s%s%s' % \
				  (verb, first_file, num - 1, ftype, plural, suffix)
	show_status_message(message, timeout_secs=3)