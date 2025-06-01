package main

import (
	"os"

	"github.com/therecipe/qt/widgets"
)

func main() {
	// Create application
	app := widgets.NewQApplication(len(os.Args), os.Args)

	// Create main window
	window := widgets.NewQMainWindow(nil, 0)
	window.SetWindowTitle("JGlossator")
	window.SetMinimumSize2(800, 600) // Set a reasonable minimum size

	// --- Main Content Area ---
	mainTextEdit := widgets.NewQTextEdit(nil)
	mainTextEdit.SetReadOnly(true) // Assuming this is for display
	mainTextEdit.SetHtml(`
		<body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 14px;">
			<h1 style="font-size: 28px; color: #50fa7b; margin-bottom: 2px;">昨日すき焼きを食べました</h1>
			<p style="font-size: 16px; color: #bd93f9; margin-top: 0px; margin-bottom: 15px;">きのう すきやき を たべました</p>

			<div style="margin-bottom: 15px;">
				<p style="font-size: 18px; color: #f8f8f2; margin-bottom: 3px;">
					昨日 <span style="color: #bd93f9;">きのう、さくじつ</span> <span style="color: #8be9fd;">2880</span>
					<span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 12px;">EDICT</span>
				</p>
				<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(n-adv, n-t) yesterday. (P)</p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 彼は昨日東京からやってきました。 <span style="color: #b0b0b0;">He came from Tokyo yesterday.</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 彼は昨日買った車を気に入っているようだ。 <span style="color: #b0b0b0;">He looks pleased with his new car which he bought yesterday.</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 彼は昨日私に会いに来るのを忘れた。 <span style="color: #b0b0b0;">He forgot to come to see me yesterday.</span></p>
			</div>

			<div style="margin-bottom: 15px;">
				<p style="font-size: 18px; color: #f8f8f2; margin-bottom: 3px;">
					すき焼き <span style="color: #bd93f9;">すきやき</span> <span style="color: #8be9fd;">048007</span>
					<span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 12px;">EDICT</span>
				</p>
				<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(n) (food) sukiyaki, thin slices of beef, cooked with various vegetables in a table-top cast-iron pan; (P)</p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> この日曜日にすき焼きパーティーをする事になっている。 <span style="color: #b0b0b0;">We're having a sukiyaki party this Sunday.</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> すき焼きはどんな材料を使うのですか。 <span style="color: #b0b0b0;">What is sukiyaki made of?</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> どうかすきやきの料理のしかたを教えて下さい。 <span style="color: #b0b0b0;">Please tell me how to cook sukiyaki.</span></p>
			</div>

			<div>
				<p style="font-size: 18px; color: #f8f8f2; margin-bottom: 3px;">
					食べる <span style="color: #bd93f9;">たべる</span> <span style="color: #8be9fd;">2392</span> (polite past)
					<span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 12px;">EDICT</span>
				</p>
				<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(v1,vt) to eat ② to live on (eg a salary), to live off, to subsist on. (P)</p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 旅行中はほとんど米は食べられなかった。 <span style="color: #b0b0b0;">We were able to eat little rice during the tour.</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 夕飯はもう食べましたか。 <span style="color: #b0b0b0;">Have you had dinner?</span></p>
				<p style="color: #f8f8f2; margin-left: 15px; margin-bottom: 2px;"><span style="color: #8be9fd;">▲</span> 彼女たちは私たちに食べるものをたくさんくれた。 <span style="color: #b0b0b0;">The women gave us a lot to eat.</span></p>
			</div>
		</body>
	`)

	// --- Bottom Text Areas ---
	bottomLeftTextEdit := widgets.NewQTextEdit(nil)
	bottomLeftTextEdit.SetReadOnly(true)
	bottomLeftTextEdit.SetFixedHeight(150) // Fixed height for bottom panels
	bottomLeftTextEdit.SetHtml(`
		<body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 13px;">
			<p style="font-size: 15px; color: #ff79c6; margin-bottom: 2px;">昨 <span style="color: #8be9fd;">226 ワク</span></p>
			<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">昨日 <span style="color: #bd93f9;">1140</span></p>
			<hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
			<p style="color: #f1fa8c; margin-top: 0px;">yesterday, previous</p>
			<br>
			<p style="font-size: 15px; color: #ff79c6; margin-bottom: 2px;">日 <span style="color: #8be9fd;">1</span></p>
			<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 2px;">12</p>
			<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">ニチ、ジッ、ひ、-び、-か</p>
			<hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
			<p style="color: #f1fa8c; margin-top: 0px;">day, sun, Japan, counter for days</p>
		</body>
	`)

	bottomRightTextEdit := widgets.NewQTextEdit(nil)
	bottomRightTextEdit.SetReadOnly(true)
	bottomRightTextEdit.SetFixedHeight(150) // Fixed height for bottom panels
	bottomRightTextEdit.SetHtml(`
		<body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 13px;">
			<p style="font-size: 15px; color: #ff79c6; margin-bottom: 2px;">焼 <span style="color: #8be9fd;">1200 カ 982 ショウ</span></p>
			<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">やける</p>
			<hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
			<p style="color: #f1fa8c; margin-top: 0px;">bake, burning</p>
			<br>
			<p style="font-size: 15px; color: #ff79c6; margin-bottom: 2px;">食 <span style="color: #8be9fd;">328 ショク、ジキ</span></p>
			<p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 2px;">く(う)、た(べる) <span style="color: #bd93f9;">1472</span></p>
			<hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
			<p style="color: #f1fa8c; margin-top: 0px;">eat, food</p>
		</body>
	`)

	// Layout for bottom text areas
	bottomLayout := widgets.NewQHBoxLayout()
	bottomLayout.AddWidget(bottomLeftTextEdit, 1, 0)  // Stretch factor 1
	bottomLayout.AddWidget(bottomRightTextEdit, 1, 0) // Stretch factor 1

	bottomWidget := widgets.NewQWidget(nil, 0)
	bottomWidget.SetLayout(bottomLayout)

	// --- Main Layout ---
	centralWidget := widgets.NewQWidget(nil, 0)
	mainLayout := widgets.NewQVBoxLayout()
	mainLayout.AddWidget(mainTextEdit, 1, 0) // Main text edit takes most space
	mainLayout.AddWidget(bottomWidget, 0, 0) // Bottom widget takes fixed space due to its content's fixed height
	centralWidget.SetLayout(mainLayout)

	window.SetCentralWidget(centralWidget)

	// --- Styling (Dark Theme - Dracula-like) ---
	// This is a basic stylesheet. For more complex styling, consider loading a .qss file.
	window.SetStyleSheet(`
		QMainWindow {
			background-color: #282a36; /* Dark background */
		}
		QTextEdit {
			background-color: #282a36; /* Dark background for text edits */
			color: #f8f8f2; /* Light text */
			border: 1px solid #44475a; /* Subtle border */
			font-family: "MS Shell Dlg 2", "Arial", sans-serif; /* Common system font */
			font-size: 14px;
			padding: 8px; /* Increased padding slightly */
		}
		QScrollBar:vertical {
			border: 1px solid #1e1f29;
			background: #1e1f29;
			width: 15px;
			margin: 15px 0 15px 0;
		}
		QScrollBar::handle:vertical {
			background: #44475a;
			min-height: 20px;
			border-radius: 7px;
		}
		QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
			border: none;
			background: none;
			height: 14px;
			subcontrol-position: top;
			subcontrol-origin: margin;
		}
		QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
			background: none;
		}
		QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
			background: none;
		}

		QScrollBar:horizontal {
			border: 1px solid #1e1f29;
			background: #1e1f29;
			height: 15px;
			margin: 0 15px 0 15px;
		}
		QScrollBar::handle:horizontal {
			background: #44475a;
			min-width: 20px;
			border-radius: 7px;
		}
		QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
			border: none;
			background: none;
			width: 14px;
			subcontrol-position: left; /* or right */
			subcontrol-origin: margin;
		}
		QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
			background: none;
		}
		QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
			background: none;
		}
	`)

	// Show the window and run the application
	window.Show()
	app.Exec()
}
