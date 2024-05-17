#include<stdio.h>
#include<string.h>
typedef struct{
    char name[7];
    int score;
}Person;
void printScoreStars(Person* persons, int len1){
    int n;
    n=((*persons).score-((*persons).score)%5)/5;
    printf("%s",(*persons).name);
    for(int i=0;i<7-len1;i++){
        printf(" ");
    }
    for(int i=0;i<n;i++){
        printf("*");
    }
    printf("\n");
}
int main(){
    Person p1,p2,p3;
    Person* pp1=&p1;
    Person* pp2=&p2;
    Person* pp3=&p3;
    scanf("%s %d",p1.name,&p1.score);
    scanf("%s %d",p2.name,&p2.score);
    scanf("%s %d",p3.name,&p3.score);
    printScoreStars(pp1,strlen(p1.name));
    printScoreStars(pp2,strlen(p2.name));
    printScoreStars(pp3,strlen(p3.name));
    
}