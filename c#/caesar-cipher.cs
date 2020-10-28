using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    // Complete the caesarCipher function below.
    static string caesarCipher(string s, int k) {

        string retVal = "";
        int pointer = k;

        pointer %= 26;

        for (int i = 0; i < s.Length; i++)
        {
            int a = Convert.ToInt32(s[i]);
            
            if((a >= 65 && a <= 90))
            {
               if (a + pointer > 90)
                    retVal  += (char) (pointer - Math.Abs(a - 90) + 64);
                else
                    retVal  += (char) (a + pointer);
            }
            else if ((a >= 97 && a <= 122))
            {
               if (a + pointer > 122)
                    retVal  += (char) (pointer - Math.Abs(a - 122) + 96);
                else
                    retVal  += (char) (a + pointer);
            }
            else {
                 retVal  += (char) (a);
            }
        }
        return retVal;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        string s = Console.ReadLine();

        int k = Convert.ToInt32(Console.ReadLine());

        string result = caesarCipher(s, k);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
