using System;

namespace PE
{
    class e15
    {
        /// <summary>
        /// The number of paths available is the sum of the number of paths to the right and below the position. 
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            long size = 21;
            var pathCount = new long[size, size];
            for (int x = 0; x < size; x++)
            {
                pathCount[x, size-1] = 1;
                pathCount[size-1, x] = 1;
            }

            for (long x = size-2; x >= 0; x--)
            {
                pathCount[x, x] = pathCount[x + 1, x] + pathCount[x, x + 1];
                for(long i = x-1; i >= 0; i--)
                {
                    pathCount[i, x] = pathCount[i + 1, x] + pathCount[i, x + 1];
                    pathCount[x,i] = pathCount[i + 1, x] + pathCount[i, x + 1];
                }
            }
            Console.WriteLine(pathCount[0, 0]);
        }
    }
}
