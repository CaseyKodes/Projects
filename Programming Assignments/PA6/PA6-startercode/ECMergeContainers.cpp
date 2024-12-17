// Created by Y. Wu, Jan 31, 2023
// Merge lists (of any STL container type) into a single sorted list (of any STL container type)
// Duplicates allowed unless the output doesn't take duplicates (e.g., a map)
// Note: you should make your code as flexible as possible: you should allow all kinds of outputs: vector, set, etc 
// Make your code short: at most 10 lines of code (LOC) 

// now defiine ECMergeContainers ...
#include <bits/stdc++.h>

template <class R, class T>
void ECMergeContainers(const R &input, T &output)
{
    output.clear();
    for (auto x : input)
    {
        copy(x.begin(), x.end(), inserter(output, output.end()));
    }
    sort(output.begin(), output.end());
}