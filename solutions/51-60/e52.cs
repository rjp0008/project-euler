using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
namespace pecs
{
    class e52
    {
        public static void Main()
        {
            int starting = 1;
            while (true)
            {
                if (HasSameDigits(starting * 2, starting * 3))
                    if (HasSameDigits(starting * 2, starting * 4))
                        if (HasSameDigits(starting * 2, starting * 5))
                            if (HasSameDigits(starting * 2, starting * 6))
                                break;
                starting++;
            }
        }

        private static bool HasSameDigits(int first,int second)
        {
            foreach (char digit in first.ToString().ToCharArray())
            {
                if (!second.ToString().ToCharArray().Contains(digit))
                    return false;
            }
            foreach (char digit in second.ToString().ToCharArray())
            {
                if (!first.ToString().ToCharArray().Contains(digit))
                    return false;
            }
            return true;
        }
    }
}
