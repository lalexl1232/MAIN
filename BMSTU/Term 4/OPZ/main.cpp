#include <iostream>
#include <stack>
#include <string>

using namespace std;

int priority(char op) {  // функция приоритета оператора
    if ((op == '+') ||  (op == '-')) return 1;
    if ((op == '*' ) ||  (op == '/')) return 2;
    return 0;
}

string toPostfix(string infix) {  // функция преобразования в ОПЗ
    stack<char> s;
    string postfix = "";
    for (int i = 0; i < infix.length(); i++) {
        if (isdigit(infix[i])) {
            postfix += infix[i];
        }
        else if (infix[i] == '(') {
            s.push('(');
        }
        else if (infix[i] == ')') {
            while (!s.empty() && s.top() != '(') {
                postfix += s.top();
                s.pop();
            }
            s.pop();
        }
        else {
            while (!s.empty() && priority(s.top()) >= priority(infix[i])) {
                postfix += s.top();
                s.pop();
            }
            s.push(infix[i]);
        }
    }
    while (!s.empty()) {
        postfix += s.top();
        s.pop();
    }
    return postfix;
}

bool is_operator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

// Функция, которая вычисляет значение двух чисел, используя оператор
double apply_operator(char op, double operand1, double operand2) {
    switch (op) {
        case '+':
            return operand1 + operand2;
        case '-':
            return operand1 - operand2;
        case '*':
            return operand1 * operand2;
        case '/':
            return operand1 / operand2;
        default:
            cerr << "Неизвестный оператор: " << op << endl;
            exit(EXIT_FAILURE);
    }
}

// Функция, которая вычисляет результат ОПЗ
double evaluate_expression(string expression) {
    stack<double> operand_stack;
    double operand1, operand2;
    char op;

    for (int i = 0; i < expression.length(); i++) {
        if (isdigit(expression[i])) { // Если символ является цифрой, то помещаем число в стек
            operand_stack.push(expression[i] - '0');
        }
        else if (is_operator(expression[i])) { // Если символ является оператором, то получаем два последних операнда из стека и применяем к ним оператор
            operand2 = operand_stack.top();
            operand_stack.pop();
            operand1 = operand_stack.top();
            operand_stack.pop();
            op = expression[i];
            operand_stack.push(apply_operator(op, operand1, operand2));
        }
    }

    return operand_stack.top(); // Возвращаем результат из стека
}

int main() {
    string infix = "((7+2)*3+3-7)"; // входное выражение
    // cin >> infix;
    string postfix = toPostfix(infix);
    cout << postfix << endl;  // вывод ОПЗ
    double result = evaluate_expression(postfix);
    cout << "result: " << result << endl;
    return 0;
}