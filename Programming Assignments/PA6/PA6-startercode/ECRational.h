#ifndef ECRational_h
#define ECRational_h


// *****************************************************************
// Generic rational of two quantities (e.g. integers, floating point, complex number, or polynomila)
// Assume the quantity class T supports (i) default constructor and copy constructor, (ii) assignment operator, and (iii) arithmatic operators: +, -, * and /
// Note: you don't need to simplify the rational. That is, it is OK to have common factors in numerator and denominoator. For example, 4/4 = 1/1

template <class T>
class ECRational
{
public:
    // YW: change the following code if needed...
    ECRational();   //constructor
    
    ECRational(const T &numeratorIn, const T &denominatorIn) : top(numeratorIn), bottom(denominatorIn) {}  
    //constructor for numerator and denominator

    ECRational(const T &numeratorIn) : top(numeratorIn), bottom(1) {}   
    //constructor for only numerator
    
    // copy constructor
    ECRational(const ECRational &other) : top(other.top), bottom(other.bottom) {}
 
    // assignment operator
    ECRational& operator=(const ECRational &other);
    
    // operators: define +, -, *, / operators yourself
    //operator for add
    friend ECRational operator+(const ECRational &l, const ECRational &r) {
        return ECRational(l.top * r.bottom + r.top * l.bottom, l.bottom * r.bottom);
    }
    //operator for sub
    friend ECRational operator-(const ECRational &l, const ECRational &r) {
        return ECRational(l.top * r.bottom - r.top * l.bottom, l.bottom * r.bottom);
    }
    //operator for multiplication
    friend ECRational operator*(const ECRational &l, const ECRational &r) {
        return ECRational(l.top * r.top, l.bottom * r.bottom);
    }
    //operator for divide
    friend ECRational operator/(const ECRational &l, const ECRational &r) {
        return ECRational(l.top * r.bottom, l.bottom * r.top);
    }

    // access numerator and denominator
    const T &GetNumerator() 
    {
        return top;
    } 
    const T &GetDenominator()
    {
        return bottom;
    }
    
private:
    // your code
    T top;
    T bottom;
};

template <class T>
ECRational<T>::ECRational() : top(T()), bottom(T(1)) {}

// assignment operator
template <class T>
ECRational<T>& ECRational<T>::operator=(const ECRational& other) {
    if (this != &other) {
        top = other.top;
        bottom = other.bottom;
    }
    return *this;
}

template class ECRational<int>;

#endif /* ECRational_h */