#ifndef ECPolynomial_h
#define ECPolynomial_h

#include <vector>
#include <cmath>
# include <algorithm>
#include <iostream>
using namespace std;

// *****************************************************************
// Represent a polynomial of a single variable, x, and
// support common operations on polynomial: add, scaling, multiple
// and (long) division, etc

class ECPolynomial
{
    public:
        // Feel free to add more interface or implementation functions
        // Construct a polynomial with coefficients, where the first position is the constant term and [i] is the coefficient of x^i
        // Example: given [1, 3, 0, 2], polynomial = 1 + 3x + 2x^3
        // We assume listCoeffsIn is not empty
        // Note: the last term in listCoeffsIn should not be zero (unless its length is 1). For example, if given [1, 3, 0], we should 
        // simply it to [1,3]. Since coefficient is a double, we consider a value is practically zero if its absolute value is 
        // sufficiently small (say less than 1e^(-10)
        ECPolynomial(const std::vector<double> &listCoeffsIn) : values(listCoeffsIn)
        {
            while (!values.empty() && fabs(values.back()) < 1e-10) 
            {  
                values.pop_back();
            }
        }
        
        ECPolynomial(int highest)
        {
            for (int i=0; i<highest+1; i++)
            {
                values.push_back(0);
            }
        }
        // Copy constructor
        ECPolynomial(const ECPolynomial &rhs) : values(rhs.values){}
    
        // Get the degree. Example: if polynomial=1+x+3x^3, degree=3
        int GetDegree() 
        { 
            if (values.empty())
            {
                return 0;
            }
            return values.size()-1; 
        }
    
        // Scale by a constant and return the resulting polynomial. For example, if polynomial is 1+3x, and
        // factor = 2, the result is 2+6x
        ECPolynomial Scale(double factor) // confused on how you would return a polynomial
        {
            vector <double> toAdd;
            for (auto x : values)
            {
                toAdd.push_back(x*factor);
            }
            return ECPolynomial(toAdd); /* need to return a polynomial */
        }
    
        // Add a polynomial to the current polynomial (and return the result). Example: (1+2x) + (2x+3x^2) = 1+4x+3x^2
        ECPolynomial operator+(const ECPolynomial &rhs) const
        {
            vector <double> sum;

            int i=0;
            while (i<values.size() && i<rhs.values.size())
            {
                sum.push_back(values[i]+rhs.values[i]);
                i++;
            }
            if (i>=values.size())
            {
                while(i<rhs.values.size())
                {
                    sum.push_back(rhs.values[i]);
                    i++;
                }
            }
            else 
            {
                while(i<values.size())
                {
                    sum.push_back(values[i]);
                    i++;
                }
            }
            return ECPolynomial(sum);
        }

        ECPolynomial operator-(const ECPolynomial &rhs) const
        {
            vector <double> difference;

            int i=0;
            while (i<values.size() && i<rhs.values.size())
            {
                difference.push_back(values[i]-rhs.values[i]);
                i++;
            }
            if (i>=values.size())
            {
                while(i<rhs.values.size())
                {
                    difference.push_back(-1*rhs.values[i]);
                    i++;
                }
            }
            else 
            {
                while(i<values.size())
                {
                    difference.push_back(values[i]);
                    i++;
                }
            }
            return ECPolynomial(difference);
        }
    
        // Multiply a polynomial by another polynomail and return the result. Example: (1+2x)*(1-x^2) = 1 + 2x - x^2 -2x^3
        ECPolynomial operator*(ECPolynomial &rhs)
        {
            vector <double> end (values.size()+rhs.values.size()-1, 0.0);
            // end is now vector with all 0 of the degree we need for the final result

            for (int j=0; j<values.size()-1; j++)
            {
                for (int k=0; k<rhs.GetDegree(); k++)
                {
                    end[j+k] += values[j]*rhs.values[k];
                }
            }
            return ECPolynomial(end);
        }
    
        // Divide a polynomial by another, and return the quotient 
        // (and save the remainder to the passed in parameter called remainder)
        // Example: if we divide x^3-2x^2-4 by x-3, then quotient = x^2+x+3 and remainder is 5
        // For now, assume rhs (denominator) is zero
        ECPolynomial operator/(ECPolynomial &rhs) 
        {
            vector<double> quotient;
            vector<double> remainder = values;
            while (!remainder.empty() && remainder.size() >= rhs.values.size()) {
                double s = remainder.back() / rhs.values.back();    //scaling 
                int d = remainder.size() - rhs.values.size(); 
                quotient.insert(quotient.begin(), s);
                for (int i = 0; i < rhs.values.size(); i++) {
                    remainder[d + i] -= s * rhs.values[i];   //multiplies the coeff by scale factor, subtracts from remainder
                }
                while (!remainder.empty() && fabs(remainder.back()) < 1e-10) 
                { 
                    remainder.pop_back();
                }
            }
            return ECPolynomial(quotient);
        }

        // related operator: remainder
        ECPolynomial operator%(ECPolynomial &rhs) 
        {
            vector<double> remainder = values;

            while (!remainder.empty() && remainder.size() >= rhs.values.size()) 
                {
                double s = remainder.back() / rhs.GetDegree();
                int d = remainder.size() - rhs.values.size();

                for (int i = 0; i < rhs.values.size(); i++) 
                {
                    remainder[d + i] -= s * rhs.values[i];
                }
                while (!remainder.empty() && fabs(remainder.back()) < 1e-10) 
                {
                    remainder.pop_back();
                }
            }
            return ECPolynomial(remainder); //returns the remainder
        }
    
        // This is for testing only. It can be useful to dump out the polynomial (in some format) to the terminal for debugging
        void Dump()
        {
            cout << values[0];
            for (int i=1; i<values.size()-1; i++)
            {
                std::cout << " + " << values[i] << "x^" << i;
                if (i==GetDegree()-1)
                {
                    cout << endl;
                    return;
                }
            }
            cout << endl;
        }

        void SetCoeffAt(int index, double value)
        {
            if (index<values.size())
            {
                values[index] = value;
            }
        }

        double GetCoeff(int index)
        {
            if(index<values.size())
            {
                return values[index];
            }
            return 0.0;
        }
    
    private:
       std::vector<double> values;
};

#endif /* ECPolynomial_h */