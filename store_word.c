#include<stdio.h>
#include<string.h>
int main(){
    int i=0;
    int c=0;
    char str[10];
    char word_list[10][10];
    while (i<10){
        c=0;
        printf("Enter a word(Enter 'end'to quit): ");
        scanf("%s",str);
        if(strcmp(str,"end")==0){
            break;
        }
        for (int x = 0; x < 5; x++){
            if (strcmp(str,word_list[x])==0){
                printf("This word already exists. Please enter another word.\n");
                c=1;
            }
        }
        if(c==0){
            strcpy(word_list[i],str);
            i++;
        }
    }

    printf("%d words in the list:\n",i);
    for(int x=0; x<i; x++){
        printf("%s ",word_list[x]);
    }
    printf("\n");
    while (1){
        c=0;
        printf("Enter a word to search(Enter 'end'to quit): ");
        scanf("%s",str);
        if(strcmp(str,"end")==0){
            break;
        }
        for (int x = 0; x < 5; x++){
            if (strcmp(str,word_list[x])==0){
                printf("This word is in the list.\n");
                c=1;
            }
        }
        if (c==0){
            printf("This word is NOT in the list.\n");
        }
    }
    
}