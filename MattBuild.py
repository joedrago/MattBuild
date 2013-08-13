import sublime, sublime_plugin
import os

os.environ["MATTBUILD"] = ""

class MattBuildCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("MattBuild Args:", os.environ["MATTBUILD"], self.on_done, None, None)

    def on_done(self, user_input):
        sublime.status_message("Setting MATTBUILD: " + user_input)
        os.environ["MATTBUILD"] = user_input

        self.view.window().run_command('build')
