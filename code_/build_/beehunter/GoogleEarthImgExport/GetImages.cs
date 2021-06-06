using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;

namespace GoogleEarthImgExport
{
    class GetImages
    {
        [DllImport("user32.dll")]
        static extern bool SetCursorPos(int x, int y);

        [DllImport("user32.dll")]
        private static extern void mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);

        private const int MOUSEEVENTF_LEFTDOWN = 0x0002;
        private const int MOUSEEVENTF_LEFTUP = 0x0004;
        private const int MOUSEEVENTF_WHEEL = 0x0800;

        private List<string> locations = new List<string>
        {
            "44.9357,-93.802742",
            "46.15262985,-96.02955627",
            "43.96575165,-97.69973755",
            "30.013973,-94.92438",
            "37.041591,-120.847117"
        };

        internal GetImages()
        {
            OpenGE();


        }
        private void OpenGE()
        {
            var processParameters = new ProcessStartInfo();
            processParameters.Arguments = "";
            processParameters.FileName = @"C:\Program Files\Google\Google Earth Pro\client\googleearth.exe";
            processParameters.WindowStyle = ProcessWindowStyle.Hidden;
            processParameters.CreateNoWindow = false;
            processParameters.UseShellExecute = false;

            using (var proc = Process.Start(processParameters))
            {
                Thread.Sleep(6000);

                foreach (var location in locations)
                {
                    Thread.Sleep(500);
                    GetLocationImage(location);
                }

                proc.WaitForExit();

            }
        }
        private void GetLocationImage(string imgLocation)
        {
            ClickMouse(100, 80, 0); // Triple click at search bar to select all
            ClickMouse(100, 80, 0);
            ClickMouse(100, 80, 0);
            Thread.Sleep(500);
            EnterText("{DEL}");
            Thread.Sleep(500);
            EnterText(imgLocation);
            EnterText("~");
            Thread.Sleep(2500);
            ScrollMouse(908, 452, 22); // Zoom at location
            Thread.Sleep(500);
            ClickMouse(700, 60, 0); // Open save image options
            Thread.Sleep(1000);
            ClickMouse(450, 120, 0); // Click the options button twice
            ClickMouse(450, 120, 0);
            Thread.Sleep(500);
            ClickMouse(910, 400, 0); // Triple click at text box to select all
            ClickMouse(910, 400, 0);
            ClickMouse(910, 400, 0);
            EnterText("{DEL}");
            Thread.Sleep(500);
            ClickMouse(910, 400, 0);
            EnterText(imgLocation);
            ClickMouse(700, 375, 0); // Close dialogue box
            Thread.Sleep(100);
            ClickMouse(300, 80, 0); // Open image options
            Thread.Sleep(100);
            ClickMouse(300, 160, 0); // Disable legend
            Thread.Sleep(500);
            ClickMouse(600, 80, 0); // Click the save image button
            Thread.Sleep(500);
            EnterText(imgLocation);
            Thread.Sleep(500);
            EnterText("~");
            Thread.Sleep(500);
            ClickMouse(800, 420, 0); // Overwrite save if file already exists
            Thread.Sleep(500);
            ClickMouse(700, 60, 0); // Close save image options
        }

        private void ClickMouse(int xloc, int yloc, int duration)
        {
            SetCursorPos(xloc, yloc);
            mouse_event(MOUSEEVENTF_LEFTDOWN, xloc, yloc, 0, 0);
            Thread.Sleep(duration);
            mouse_event(MOUSEEVENTF_LEFTUP, xloc, yloc, 0, 0);
        }
        private void ScrollMouse(int xloc, int yloc, int rotation)
        {
            SetCursorPos(xloc, yloc);
            for (int i = 0; i <= rotation; i++)
            {
                mouse_event(MOUSEEVENTF_WHEEL, xloc, yloc, 120, 0);
                Thread.Sleep(300);
            }
        }
        private void EnterText(string textToEnter)
        {
            SendKeys.SendWait(textToEnter);
        }
    }
}
