#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    cout << "start";
    int count = 0;
    char* buf = new char[16];
    ifstream f("190829_v29854.KNP", ios::binary);
    while (!f.eof())
    {
        f.read(buf, 16);
        if (count < 0x200 || count > 0xd41000) {
            cout << setw(8) << setfill('0') << count << "   ";
            for (int i = 0; i < 16; i++)
            {
                cout << setw(2) << setfill('0') << hex << int(buf[i] & 0xff) << ' ';
                if (i == 7)
                {
                    cout << "   ";
                }
            }
            cout << endl;
        }
        count += 16;
    }
    delete[] buf;
    f.close();
    ifstream file("190829_v29854.KNP", ios::binary);
    char buff[16];

    f.close();
    return 0;
} 