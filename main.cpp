//
// Created by Nolan Jimmo on 4/8/2020.
//
#include <fstream>
#include <iostream>
using namespace std;

#ifdef _WIN32
const string python = "python";
#else
const string python = "python3";
#endif

string getResponse(string prompt);

int main(){
    cout << "Welcome to our scatter plotting service! Enter your responses to the questions below to receive the graph output of your .csv data set." << endl;
    string title = getResponse("Title of graph: ");
    string varX = getResponse("Label for x variable: ");
    string varY = getResponse("Label for y variable: ");
    string dataFile = getResponse("Enter the .csv file where your data is held (ex. myfile.csv): ");

    string command = python + " graph.py " + dataFile + " " + title + " " + varX + " " + varY;
    system(command.c_str());

    return 0;
}

string getResponse(string prompt){
    string response;
    cout << prompt;
    getline(cin, response);
    response = '"' + response + '"';
    return response;
}
