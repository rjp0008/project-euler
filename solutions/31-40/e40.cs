using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pecs
{
    class e40
    {
        static void Main(string[] args)
          {
            StringBuilder test = new StringBuilder("");
            for (int i = 1; i <= 1000000; i++)
            {
                test.Append(i.ToString());
            }
            int output = int.Parse(test[0].ToString());
            output *= int.Parse(test[9].ToString());
            output *= int.Parse(test[99].ToString());
            output *= int.Parse(test[999].ToString());
            output *= int.Parse(test[9999].ToString());
            output *= int.Parse(test[99999].ToString());
            output *= int.Parse(test[999999].ToString());
            Console.WriteLine(output);
            Console.ReadLine();

        }
    }
}
