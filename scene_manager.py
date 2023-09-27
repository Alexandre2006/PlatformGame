# Scene Manager
# Written by Copilot (except unregister_scene)
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def register_scene(self, scene_name, scene_instance):
        self.scenes[scene_name] = scene_instance
    
    def unregister_scene(self, scene_name):
        if scene_name in self.scenes:
            del self.scenes[scene_name]
        else:
            print(f"Scene '{scene_name}' does not exist.")

    def switch_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]
        else:
            print(f"Scene '{scene_name}' does not exist.")

    def update_current_scene(self):
        if self.current_scene:
            self.current_scene.update()

    def render_current_scene(self):
        if self.current_scene:
            self.current_scene.render()

    def handle_events(self, events):
        if self.current_scene:
            self.current_scene.handle_events(events)