using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pecs
{
    class e112
    {
        static void Main(string[] args)
        {
            double ratio = 0;
            int bouncy = 0;
            int nonbouncy = 0;
            while (ratio < .99)
            {
                if (isBouncy(bouncy + nonbouncy + 1))
                    bouncy++;
                else
                    nonbouncy++;
                ratio = bouncy * 1.0 / (bouncy + nonbouncy);
            }
            Console.WriteLine(bouncy + nonbouncy);
            Console.ReadLine();
        }

        private static bool isBouncy(int input)
        {
            bool increasing = false;
            bool decreasing = false;
            for (int i = 0; i < input.ToString().Length - 1; i++)
            {
                for (int y = i + 1; y < input.ToString().Length; y++)
                {
                    if (((int)input.ToString().ToArray()[i]) > ((int)input.ToString().ToArray()[y]))
                    {
                        decreasing = true;
                    }
                    if (((int)input.ToString().ToArray()[i]) < ((int)input.ToString().ToArray()[y]))
                    {
                        increasing = true;
                    }
                }
            }
            return increasing && decreasing;
        }
    }
}
