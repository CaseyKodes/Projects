#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <ctype.h>
#include <assert.h>

#define MAX 10240
#define MAX_WORD_COUNT 60000                //we have less than 60000 words
#define MAX_WORD_LENGTH 80                  //each word is less than 80 letters

//Using these two global variables can be justified :)
char words[MAX_WORD_COUNT][MAX_WORD_LENGTH];        //2-d array to hold all the words
int word_count = 0;                                 //number of words, initilized to 0

//Note the words in the dictionary file are sorted
//This fact could be useful
void read_file_to_array(char *filename)
{
    FILE *fp;

    //open the file for reading
    fp = fopen(filename, "r");
    if(fp==NULL)
    {
        printf("Cannot open file %s.\n", filename);
        exit(-1);
    }
    //make sure when each word is saved in the array words,
    //it does not ends with a '\n'
    //see how this is done using fscanf 
    while(!feof(fp))
        fscanf(fp, "%s\n", words[word_count++]);
    fclose(fp);
}

//TODO
//Test wether a string word is in the dictionary
//Return 1 if word is in the dictionary
//Return 0 otherwise
//Be efficient in implementing this function
//Efficiency is needed to pass test cases in limited time
int in_dict(char *word)
{
    /*
    strcmp to compare strings
    strcmp(str1, str2)
    if = returns 0
    if str1 > str 2 returns integers > 0
    if str1 < str2 returns integer < 0
    */
    if (word == NULL)
    {
        return 0;
    }
    int left = 0;
    int right = MAX_WORD_COUNT; 
    int mid;
    while (left<right)
    {
        mid = (left+right)/2;

        if (strcmp(word, words[mid])==0) //equal 
        {
            return 1;
        }
        else if (strcmp(word, words[mid]) > 0 ) // word bigger than half
        {
            left = mid+1;
        }
        else //if (strcmp(word, words[mid]) < 0 ) // word smaller than half 
        {
            right = mid-1;
        }
    }
    return 0;
}

//TODO
//Use key and shift to decrypt the encrypted message
//len is the length of the encrypted message
//Note the encrypted message is stored as an array of integers (not chars)
//The result is in decrypted
void decryption(unsigned char key, unsigned char shift, const int *encrypted, int len, char *decrypted)
{
    /*
    just need to do the reverse of encryption
    xor then shift
    */
    char data;
    for(int i = 0; i < len; i++) 
    {
        data = (char)((encrypted[i]^key) >> shift);
        decrypted[i] = data;
    }
    decrypted[len] = '\0';
}

//TODO
//calculate a score for a message msg
//the score is used to determine whether msg is the original message
int message_score(const char *msg)
{
    /* 
    loop through message and for each word in message 
    check if they are in dictionary if they are increase score
    */

    int score = 0;
    int len = strlen(msg);
    if (len == 0) 
    {
        return 0;
    }
    int charAt = 0;
    char buff[len];
    for(int i = 0; i <= len; i++) 
    {
        if(isalpha(msg[i])) 
        {
            buff[charAt] = msg[i];
            charAt++;
        }
        else if (msg[i]== ' ' || msg[i]== '\0')//seeing if char is not alpha
        {
            buff[charAt] = '\0';
            if(in_dict(buff)) 
            {
                score += 1;
            }
            charAt = 0;
        }
    }
    return score;
}

//read the encrypted message from the file to encrypted
//return number of bytes read
int read_encrypted(char *filename, int *encrypted)
{
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) 
    {
        printf("File opening error");
        exit(-1);
    }
    int count = 0;
    while (fread(&encrypted[count], sizeof(int), 1, fp)) 
    {
        ++count;
    }
    fclose(fp);
    return count;
}

//search using all the (key, shift) combinations
//to find the original message
//result is saved in message
void search(const int *encrypted, int len, char *message)
{
	char decrypted[MAX];
    int max_score = 0;
    strcpy(message, "");
    for(unsigned char k = 0; k < 255; k++)
    {
        for(unsigned char shift = 0; shift <= 24; shift++)
        {
            decryption(k, shift, encrypted, len, decrypted);
			int score = message_score(decrypted);
			if(score > max_score)
			{	
				max_score = score;
				strcpy(message, decrypted);
			}
        }
    }
}

//Do not change the main() function
int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("%s encrypted-message\n", argv[0]);
		return 0;
	}

	read_file_to_array("dict.txt");

	int encrypted[MAX];
	int len = read_encrypted(argv[1], encrypted);
	
	char message[MAX];
	strcpy(message, "");
	search(encrypted, len, message);
	printf("%s\n", message);
	return 0;
}