using System;

namespace PE
{
    class e19
    {
        static void Main(string[] args)
        {
            Console.WriteLine(SundayCounter(new DateTime(1901, 1, 1), new DateTime(2000, 12, 31)));
        }

        /// <summary>
        /// Counts the number of Sundays that start the month from first parameter to second parameter.
        /// </summary>
        /// <param name="startDate">The date to start the search.</param>
        /// <param name="finishDate">The date to end the search.</param>
        /// <returns></returns>
        static int SundayCounter(DateTime startDate, DateTime finishDate)
        {
            int totalSundays = 0;
            startDate = GetNextSunday(startDate);

            while (startDate < finishDate)
            {
                if (startDate.Day == 1)
                {
                    totalSundays++;
                }

                startDate = startDate.AddDays(7);
            }

            return totalSundays;
        }

        /// <summary>
        /// Returns the next possible DateTime that is a Sunday.
        /// </summary>
        /// <param name="input"></param>
        /// <returns></returns>
        static DateTime GetNextSunday(DateTime input)
        {
            if (input.DayOfWeek == DayOfWeek.Sunday)
            {
                return input;
            }

            int numberOfDaysUntilSunday = 7 - (int)input.DayOfWeek;
            return input.AddDays(numberOfDaysUntilSunday);
        }
    }
}
