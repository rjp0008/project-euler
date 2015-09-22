using System.Collections.Generic;
using System.IO;

namespace PE
{
    class e67
    {

        static void Main(string[] args)
        {
           var file = File.OpenText("p067_triangle.txt");
            List<string> rows = new List<string>();
            while (!file.EndOfStream)
            {
               rows.Add(file.ReadLine());
            }
            List <List<int>> ints = new List<List<int>>();
            foreach (string item in rows)
            {
                List<int> thisList = new List<int>();
                foreach (string number in item.Split(' '))
                {
                    thisList.Add(int.Parse(number));
                }
                ints.Add(thisList);
            }
            ints.Reverse();
            int[] oldMax = null;
            foreach (var row in ints)
            {
                var maxValue = new int[row.Count];
                for (int x = 0; x < row.Count; x++)
                {
                    maxValue[x] = row[x];
                    if (oldMax != null)
                    {
                        maxValue[x] += oldMax[x] > oldMax[x + 1] ? oldMax[x] : oldMax[x + 1];
                    }
                }
                oldMax = maxValue;
            }

        }



    }
}
