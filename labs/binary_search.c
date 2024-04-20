int     binary_search(int a[], int n, int v)
{
    int     rv;

    if (n == 0) {        // nothing in the array
        rv = -1;
        goto  f_exit;    // return -1
    }

    int half = n / 2;   // integer division
    int half_v = a[half];

    if (half_v == v) {
        rv = half;
    }
    else if (v < half_v) {
        // search the first half, excluding a[half]
        rv = binary_search(a, half, v); 
    }
    else {  // v > half_v
        // search the second half, excluding a[half]
        int left = half + 1;

        // &a[left] means the address of a[left]
        rv = binary_search(&a[left], n - left, v);

        if (rv >= 0) {
            rv += left;
        }
    }

f_exit:
    return rv;
}