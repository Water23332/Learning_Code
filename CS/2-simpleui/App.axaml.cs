using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;

namespace JGlossator // Match your project's namespace
{
    public partial class App : Application
    {
        public override void Initialize()
        {
            AvaloniaXamlLoader.Load(this);
        }

        public override void OnFrameworkInitializationCompleted()
        {
            if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
            {
                desktop.MainWindow = new MainWindow(); // Creates an instance of your main window
            }
            // For single view applications (like mobile or WASM)
            else if (ApplicationLifetime is ISingleViewApplicationLifetime singleViewPlatform)
            {
                // This part might not be relevant for a desktop JGlossator
                // singleViewPlatform.MainView = new MainView(); // Or your initial view
            }

            base.OnFrameworkInitializationCompleted();
        }
    }
}
