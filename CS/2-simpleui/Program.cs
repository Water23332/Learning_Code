using Avalonia;
using System;

namespace JGlossator // Match your project's namespace
{
    class Program
    {
        // Initialization code. Don't use any Avalonia, third-party APIs or any
        // SynchronizationContext-reliant code before AppMain is called: things aren't initialized
        // yet and stuff might break.
        [STAThread]
        public static void Main(string[] args) => BuildAvaloniaApp()
            .StartWithClassicDesktopLifetime(args);

        // Avalonia configuration, don't remove; also used by visual designer.
        public static AppBuilder BuildAvaloniaApp()
            => AppBuilder.Configure<App>() // Points to your App class
                .UsePlatformDetect()
                .LogToTrace();
                // If you need Skia features, you might also have:
                // .WithInterFont()
                // .UseSkia();
    }
}
