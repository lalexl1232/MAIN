#include <iostream>
using namespace std;

template <typename TypeE>
class Univers
{
public:
    int n;
    TypeE* U;
    Univers(int nn, TypeE* u ): n(nn)
    {
        U = new TypeE[n];
        for(int i=0; i<n; i++)
            U[i]=u[i];
    }
    TypeE& operator [] (int i)
    {
        return U[i];
    }
    int N(){return n;}
};

template <typename TypeE>
class Set
{
private:
    Univers<TypeE>* Univer;
public:
    int n;
    int* shk;
    Set(Univers<TypeE>& U)
    {
        n=U.N();
        cout<<"n="<<n<<endl;
        shk=new int[n];
        for(int i=0; i<n; i++)
            shk[i]=0;
        Univer = &U;
    }
    void add(int i) // ÃÂÚÓ‰ ‰Ó·‡‚ÎÂÌËˇ ˝ÎÂÏÂÌÚ‡
    {
        shk[i]=1;
    }

     void add2(TypeE x){
         for (int i = 0; i < n; i++) {
             if((*Univer)[i] == x)
                 add(i);
         }
         print();
    }

    void print(){
        for(int i=0; i<n; i++)
        {
            if(shk[i]==1)
                cout<<(*Univer)[i]<<" ";
        }
    }
};
int main()
{
    int m[5]={0,1,2,3,4};
    Univers<int> intU(5,m);
    cout<<"intU="; for (int i=0; i<5; i++) cout<<intU[i]<<' ';
    cout<<endl;

    Set<int> s1(intU);
    cout<<"s1=";
    s1.print();
    cout<<endl;
    s1.add2(3);
    cout<<endl;
    s1.add2(4);
    cout<<endl;


    float mm[6]={0.0,1.1,2.2,3.3,4.4,5.5};
    Univers<float> floatU(6,mm);
    for (int i=0; i<6; i++)
        intU[i]=i; cout<<endl;
    cout<<"floatU=";
    for (int i=0; i<6; i++)
        cout<<floatU[i]<<' ';
    cout<<endl;

    Set<float> s2(floatU);
    cout<<"s2=";
    for(int i=0; i<6; i++)
        if(s2.shk[i]==1)
            cout<<floatU.U[i]<<" ";
    cout<<endl;

    s2.add2(3.3);
    cout<<endl;
    s2.add2(5.5);
    cout<<endl;
    return 0;
}
