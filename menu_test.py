import scene, sound

player_name = 'TJ'
MENU_FONT = 'AvenirNext-Heavy'
BUTTON_FONT = 'Arial-BoldMT'
GAME_CHARACTER = 'Boy'

class Start (scene.Scene):
    def draw(self):
        center = self.bounds.center()
        portrait = self.size.h > self.size.w
        #landscape = self.size.w > self.size.h
        scene.background(0.40, 0.80, 1.00) # light blue background color

        scene.fill(0.50, 1.00, 0.00) # play button fill color

        if portrait:
            self.play_btn_rect = scene.Rect(200, 358, 600, 100)
            self.char_btn_rect = scene.Rect(140, 485, 470, 100)
        else:
            self.play_btn_rect = scene.Rect( 20, 358, 350, 100)
            self.char_btn_rect = scene.Rect( 20, 485, 230, 100)
        
        scene.rect(*self.play_btn_rect)
        scene.fill(1.00, 1.00, 1.00) # character select button fill color
        scene.rect(*self.char_btn_rect)
        
        scene.tint(1.00, 1.00, 1.00) # white text color
        fs, x, y = (100, 385, 850) if portrait else (150, 525, 600)
        scene.text('Cloud Jump', MENU_FONT,  font_size=fs, x=x, y=y)
        fs, x, y = ( 65, 380, 650) if portrait else ( 65, 200, 400)
        scene.text('Play Game', BUTTON_FONT, font_size=fs, x=x, y=y)
        scene.tint(0.00, 0.50, 1.00) # blue text color
        fs, x, y = ( 54, 380, 521) if portrait else ( 54, 260, 285)
        scene.text('Character Select', BUTTON_FONT, font_size=fs, x=x, y=y)
        scene.tint(1.00, 1.00, 1.00) # white text color
        fs =  30
        if portrait:
            x, y = self.bounds.w / 2.0, self.bounds.h / 1.34
        else:
            x, y = self.bounds.w / 1.4, self.bounds.h / 1.7
        s = 'Welcome {}!'.format(player_name)
        scene.text(s, MENU_FONT, font_size=fs, x=x, y=y)

        for i in xrange(11):
            scene.image('PC_Grass_Block', self.bounds.w / 11 * i, 0)

    def touch_ended(self, touch):
        if touch.location in self.play_btn_rect:
            main_scene.switch_scene(#Game Scene Here)
        elif touch.location in self.char_btn_rect:
            main_scene.switch_scene('CharacterSelect1')
            
class CharacterSelect1(scene.Scene):
	def setup(self):
		center = self.bounds.center()
		global p1_rect, p2_rect, p3_rect, p4_rect, p5_rect, p6_rect

		if self.size.w > self.size.h: # landscape
			p1_rect = scene.Rect(40, 400, 250, 250)
			p2_rect = scene.Rect(395, 400, 250, 250)
			p3_rect = scene.Rect(735, 400, 250, 250)
			p4_rect = scene.Rect(40, 80, 250, 250)
			p5_rect = scene.Rect(395, 80, 250, 250)
			p6_rect = scene.Rect(735, 80, 250, 250)

		if self.size.h > self.size.w: # portrait
			p1_rect = scene.Rect(80, 735, 250, 250)
			p2_rect = scene.Rect(400, 735, 250, 250)
			p3_rect = scene.Rect(80, 395, 250, 250)
			p4_rect = scene.Rect(400, 395, 250, 250)
			p5_rect = scene.Rect(80, 80, 250, 250)
			p6_rect = scene.Rect(400, 80, 250, 250)

	def draw(self):
		global p1_rect, p2_rect, p3_rect, p4_rect, p5_rect, p6_rect
		scene.background(0.40, 0.80, 1.00)
		scene.fill(1.00, 1.00, 1.00)

		scene.image('Boy', *p1_rect)
		scene.image('Girl', *p2_rect)
		scene.image('Guardsman', *p3_rect)
		scene.image('Hamster_Face', *p4_rect)
		scene.image('Mouse_Face', *p5_rect)
		scene.image('Man', *p6_rect)

	def check(self, x, y, posx, posy, sizex, sizey):
		if x >= posx and x <= posx + sizex:
			if y >= posy and y <= posy + sizey:
				return True
		return False

	def touch_began(self, touch):
		pass

	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		x, y = touch.location
		global GAME_CHARACTER;

		if touch.location in p1_rect:
			GAME_CHARACTER = 'Boy'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		if touch.location in p2_rect:
			GAME_CHARACTER = 'Girl'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		if touch.location in p3_rect:
			GAME_CHARACTER = 'Guardsman'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		if touch.location in p4_rect:
			GAME_CHARACTER = 'Hamster_Face'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		if touch.location in p5_rect:
			GAME_CHARACTER = 'Mouse_Face'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		if touch.location in p6_rect:
			GAME_CHARACTER = 'Man'
			sound.play_effect('Ding_3')
			main_scene.switch_scene(#Game Scene Here)

		else:
			pass

class MultiScene (scene.Scene):
    def __init__(self, start_scene):
        self.active_scene = start_scene()
        scene.run(self)

    def switch_scene(self, new_scene):
        self.active_scene = new_scene()
        self.setup()

    def setup(self):
        global screen_size
        screen_size = self.size
        self.active_scene.add_layer = self.add_layer
        self.active_scene.size = self.size
        self.active_scene.bounds = self.bounds
        self.active_scene.root_layer = self.root_layer
        self.active_scene.setup()

    def draw(self):
        self.active_scene.touches = self.touches
        self.active_scene.t = self.t
        self.active_scene.dt = self.dt
        self.active_scene.draw()

    def touch_began(self, touch):
        self.active_scene.touch_began(touch)

    def touch_moved(self, touch):
        self.active_scene.touch_moved(touch)

    def touch_ended(self, touch):
        self.active_scene.touch_ended(touch)

main_scene = MultiScene(Start)
