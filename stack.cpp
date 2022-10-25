#include <iostream>
using namespace std;

class stack{
	private:
		int top;
		int arr[5];
	public:
		stack()
		{
			top=-1;
			for(int i=0;i<5;i++)
			{
				arr[i]=0;
			}
		}
	bool isempty();
	bool isfull();
	void push(int val);
	int pop();
	void display();
};
bool stack::isempty()
{
	if(top==-1)
	return true;
	else
	return false;
}
bool stack::isfull()
{
	if(top==4)
	return true;
	else
	return false;
}
void stack::push(int val)
{
	if(isfull())
	{
		cout<<"stack overflow"<<endl;
	}
	else
	{
		top++;
		arr[top]=val;
	}
}
int stack::pop()
{
	if(isempty())
	{
		cout<<"stack underflow"<<endl;
		return 0;
	}
	else
	{
		int popvalue=arr[top];
		arr[top]=0;
		top--;
		return popvalue;
	}
}
void stack::display()
{
 cout<<"All value int the stack are"<<endl;
 for(int i=4;i>=0;i--)
 {
	cout<<arr[i]<<endl;
	 }	
}
int main()
{
	stack s1;
	int op,val;
	do
	{
		cout<<"enter option"<<endl<<"1=push"<<endl<<"2=pop"<<endl<<"3=isempty"<<endl<<"4=isfull"<<endl<<"5=display"<<endl<<"6=exit"<<endl;
		cin>>op;
		switch(op)
		{
			case 1:
				cout<<"enter an iteam to psuh in the stack"<<endl;
				cin>>val;
				s1.push(val);
				break;
			case 2:
				s1.pop();
				break;
			case 3:
				if(s1.isempty())
					cout<<"stack is empty"<<endl;
					else
					cout<<"stack is not empty"<<endl;
				break;
			case 4:
				if(s1.isfull())
				cout<<"stack is full"<<endl;
				else
				cout<<"stack is not full"<<endl;
				break;
			case 5:
				cout<<"display function called"<<endl;
				s1.display();
				break;
			case 6:
				break;
		}
	}while(op!=6);
}

