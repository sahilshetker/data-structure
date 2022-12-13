#include <iostream>
#include <string>

using namespace std;

class node
{
    public:
        string Patient_name;
        int Patient_ID;
        int Patient_age;
        string disease;
        int priority;
        node *next;
};

class PriorityQueue
{
    private:
        node *front;
    public:
        PriorityQueue()
        {
            front = NULL;
        }
        int PriorityBasesOnDisease(string disease);
        void insertDetails(string name, int id, int age, string disease);
        void remove(int id);
        void display();
};


/*
    insert funtion based on priority of disease
*/
void PriorityQueue::insertDetails(string name, int id, int age, string disease)
{
    node *temp, *q;
    temp = new node;
    temp->Patient_name = name;
    temp->Patient_ID = id;
    temp->Patient_age = age;
    temp->disease = disease;
    temp->priority = PriorityBasesOnDisease(disease);
    if (front == NULL || temp->priority < front->priority)
    {
        temp->next = front;
        front = temp;
    }
    else
    {
        q = front;
        while (q->next != NULL && q->next->priority <= temp->priority)
            q=q->next;
        temp->next = q->next;
        q->next = temp;
    }
}

int PriorityQueue::PriorityBasesOnDisease(string disease)
{
    if (disease == "cancer")
        return 1;
    else if (disease == "fracture")
        return 2;
    else if (disease == "fever")
        return 3;
    else if (disease == "headache")
        return 4;
    else if (disease == "Malaria")
        return 5;
    else
        return 6;
}

void PriorityQueue::remove(int id)
{
    node *temp, *q;
    if(front->Patient_ID == id)
    {
        temp = front;
        front = front->next;
        delete temp;
    }
    else
    {
        q = front;
        while(q->next->Patient_ID != id && q->next != NULL)
        {
            q = q->next;
        }
        if(q->next == NULL)
        {
            cout << "Patient ID not found" << endl;
        }
        else
        {
            temp = q->next;
            q->next = temp->next;
            delete temp;
        }
    }
}

/*
    Priority vise display
*/
void PriorityQueue::display()
{
    node *ptr;
    ptr = front;
    if (front == NULL)
        cout << "Queue is empty" << endl;
    else
    {	cout << "Patient Name\tPatient ID\tPatient Age\tDisease\t" << endl;
        while (ptr != NULL)
        {
            cout << ptr->Patient_name << "\t\t" << ptr->Patient_ID << "\t\t" << ptr->Patient_age << "\t\t" << ptr->disease << "\t"<< endl;
            ptr = ptr->next;
        }
    }
}

int main()
{
    int choice, id, age;
    string name, disease;
    PriorityQueue pq;
    cout<<"----------------------------------------------------------------------------------------------------------------------------"<<endl<<endl;
    cout<<"\t\t\t\t\t\t HOSPITAL MANAGEMENT SYSTEM"<<endl<<endl;
    cout<<"\t\t\t\t\t\t     By Chitraksh & Sahil"<<endl;
    cout<<"----------------------------------------------------------------------------------------------------------------------------"<<endl;

    while (1)
    {
        cout << "1.Insert Patient Details" << endl;
        cout << "2.Remove Patient Details" << endl;
        cout << "3.Display Patient Details" << endl;
        cout << "4.Quit" << endl;
        cout << "Enter your choice : ";
        cin >> choice;
        switch(choice)
        {
        case 1:
        system("cls");
            cout << "Enter Patient Name : ";
            cin >> name;
            cout << "Enter Patient ID : ";
            cin >> id;
            cout << "Enter Patient Age : ";
            cin >> age;
            cout << "Enter Patient Disease : ";
            cin >> disease;
            pq.insertDetails(name, id, age, disease);
            break;
        case 2:
            cout << "Enter Patient ID : ";
            cin >> id;
            pq.remove(id);
            break;
        case 3:
            pq.display();
            break;
        case 4:
            exit(1);
        default:
            cout << "Wrong choice" << endl;
        }
    }
    return 0;
}
