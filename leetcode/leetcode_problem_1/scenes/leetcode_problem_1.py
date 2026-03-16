from manim import *
from mymanimlibrary import *





class Scene0(Scene):

	def construct(self):

		my_tex_template = TexTemplate()
		my_tex_template.add_to_preamble(r"\usepackage{xcolor}")
		my_tex_template.add_to_preamble(r"\definecolor{PURE_GREEN}{HTML}{00FF00}")

		# Title

		title_string = "Problem Description"
		ref_title_string = "Problem Description ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789,?!"

		title_tex = MyTex(rf"{title_string}", font_size = 66)
		ref_title_tex = MyTex(rf"{ref_title_string}", font_size = 66)

		ref_title_tex.to_edge(1.5 * UP)

		y_position = ref_title_tex[0][0:18].get_center()[1]

		title_tex.move_to([title_tex.get_center()[0], y_position, 0])



		# Underline
		underline = Line (
			start = [
				-3.80 * (16 / 9), 0, 0
			],
			end = [
				3.80 * (16 / 9), 0, 0
			],
			stroke_width = 2
		)

		underline.to_edge(3.1 * UP)

		# Header
		header = VGroup(title_tex, underline)


		# Sentence 1

		sen_1_string = "\\textcolor{PURE_GREEN}{Given an array of integers nums and an integer target,} return indices of the two numbers such that they add up to target."

		sen_tex_1 = MyTex(
			rf"""
			\setlength{{\fboxrule}}{{0.1pt}}
			\fbox{{%
				\begin {{minipage}} {{25em}}
				\frenchspacing
				{sen_1_string}
				\end{{minipage}}%
			}}
			""",
			tex_template = my_tex_template
		)






		# Sentence 2

		sen_2_string = "\\textcolor{PURE_GREEN}{You may assume that each input would have exactly one solution,} and you may not use the same element twice."

		sen_tex_2 = MyTex(
			rf"""
			\setlength{{\fboxrule}}{{0.1pt}}
			\fbox{{%
				\begin {{minipage}} {{25em}}
				\frenchspacing
				{sen_2_string}
				\end{{minipage}}%
			}}
			""",
			tex_template = my_tex_template
		)


		# Sentence 3

		sen_3_string = "You can return the answer in any order."


		sen_tex_3 = MyTex(
			rf"""
			\setlength{{\fboxrule}}{{0.1pt}}
			\fbox{{%
				\begin {{minipage}} {{25em}}
				\frenchspacing
				{sen_3_string}
				\end{{minipage}}%
			}}
			""",
			tex_template = my_tex_template
		)


		# Body

		sen_tex_2.set_opacity(0)
		sen_tex_3.set_opacity(0)

		body = VGroup(sen_tex_1, sen_tex_2, sen_tex_3)
		body.arrange(DOWN, aligned_edge = LEFT, buff = 1)
		body.next_to(header, DOWN, buff = 0.5)


		# Header animation
		self.wait()
		self.play(
			Succession(
				Write(title_tex),
				GrowFromCenter(underline)
			)
		)
		self.wait()

		# Body copy

		sen_tex_1_copy = sen_tex_1[0][0:-4].copy()
		sen_tex_2_copy = sen_tex_2[0][0:-4].copy()
		sen_tex_3_copy = sen_tex_3[0][0:-4].copy()

		sen_tex_1_copy.set_color(WHITE)
		sen_tex_2_copy.set_color(WHITE)
		sen_tex_3_copy.set_color(WHITE)

		body_copy = VGroup(sen_tex_1_copy, sen_tex_2_copy, sen_tex_3_copy)


		# Page

		page = VGroup(header, body_copy)

		# Sentence 1 animation

		self.play(
			Write(sen_tex_1_copy)
		)
		self.wait()

		indices_1 = sen_tex_1.get_tex_indices_by_color(PURE_GREEN)

		


		self.wait()
		self.play(
			sen_tex_1_copy[indices_1[0][0]:indices_1[0][1]].animate.set_color(PURE_GREEN)
		)
		self.wait()

		self.wait()
		self.play(
			sen_tex_1_copy[indices_1[0][0]:indices_1[0][1]].animate.set_color(WHITE)
		)
		self.wait()


		self.play(
			sen_tex_1_copy[indices_1[0][1]:].animate.set_color(PURE_GREEN)
		)
		self.wait()


		self.play(
			sen_tex_1_copy[indices_1[0][1]:].animate.set_color(WHITE)
		)
		self.wait()


		# Page animation

		self.wait()
		self.play(
			page.animate.shift((0 - body_copy[1].get_center()[1]) * UP)
		)
		self.wait()


		# Sentence 2 animation

		self.play(
			Write(sen_tex_2_copy.set_opacity(1))
		)
		self.wait()



		indices_2 = sen_tex_2.get_tex_indices_by_color(PURE_GREEN)


		self.play(
			sen_tex_2_copy[indices_2[0][0]:indices_2[0][1]].animate.set_color(PURE_GREEN)
		)
		self.wait()


		self.play(
			sen_tex_2_copy[indices_2[0][0]:indices_2[0][1]].animate.set_color(WHITE)
		)
		self.wait()


		self.play(
			sen_tex_2_copy[indices_2[0][1]:].animate.set_color(PURE_GREEN)
		)
		self.wait()


		self.play(
			sen_tex_2_copy[indices_2[0][1]:].animate.set_color(WHITE)
		)
		self.wait()


		# Page animation

		self.wait()
		self.play(
			page.animate.shift((0 - body_copy[2].get_center()[1]) * UP)
		)
		self.wait()


		# Sentence animation

		self.play(
			Write(sen_tex_3_copy.set_opacity(1))
		)
		self.wait()


		self.play(
			sen_tex_3_copy.animate.set_color(PURE_GREEN)
		)
		self.wait()





class Scene1(Scene):

	def construct(self):

		my_tex_template = TexTemplate()
		my_tex_template.add_to_preamble(r"\usepackage{xcolor}")
		my_tex_template.add_to_preamble(r"\definecolor{PURE_GREEN}{HTML}{00FF00}")

		# Title

		title_string = "Example 1"
		ref_title_string = "Problem Description ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789,?!"

		title_tex = MyTex(rf"{title_string}", font_size = 66)
		ref_title_tex = MyTex(rf"{ref_title_string}", font_size = 66)

		ref_title_tex.to_edge(1.5 * UP)

		y_position = ref_title_tex[0][0:18].get_center()[1]

		title_tex.move_to([title_tex.get_center()[0], y_position, 0])



		# Underline
		underline = Line (
			start = [
				-3.80 * (16 / 9), 0, 0
			],
			end = [
				3.80 * (16 / 9), 0, 0
			],
			stroke_width = 2
		)

		underline.to_edge(3.1 * UP)

		# Header
		header = VGroup(title_tex, underline)



		# Sentence 1

		sen_1_string = "\\textcolor{PURE_GREEN}{Input}: nums = \\textcolor{PURE_GREEN}{[3, 2, 4]}, target = 6"


		sen_tex_1 = MyTex(
			rf"""
			\setlength{{\fboxrule}}{{0.1pt}}
			\fbox{{%
				\begin {{minipage}} {{25em}}
				\frenchspacing
				{sen_1_string}
				\end{{minipage}}%
			}}
			""",
			tex_template = my_tex_template
		)


		# Sentence 2

		sen_2_string = "\\textcolor{PURE_GREEN}{Output}: [1, 2]"


		sen_tex_2 = MyTex(
			rf"""
			\setlength{{\fboxrule}}{{0.1pt}}
			\fbox{{%
				\begin {{minipage}} {{25em}}
				\frenchspacing
				{sen_2_string}
				\end{{minipage}}%
			}}
			""",
			tex_template = my_tex_template
		)

		# Body

		body = VGroup(sen_tex_1, sen_tex_2)
		body.arrange(DOWN, aligned_edge = LEFT, buff = 1)


		body.next_to(header, DOWN, buff = 0.5)


		# Body copy

		sen_tex_1_copy = sen_tex_1[0][0:-4].copy()
		sen_tex_2_copy = sen_tex_2[0][0:-4].copy()

		sen_tex_1_copy.set_color(WHITE)
		sen_tex_2_copy.set_color(WHITE)

		body_copy = VGroup(sen_tex_1_copy, sen_tex_2_copy)


		# Page
		page = VGroup(header, body_copy)


		self.add(page)


















		





