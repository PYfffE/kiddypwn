#include <stdio.h>
#include <unistd.h>

void chatting(){
    char name[200];
    sleep(3);

    printf("Victim> Hi, what's your name, hacker?\n");
    fflush(stdout);
    printf("Me> ");
    fflush(stdout);
    gets(name);
    sleep(1);

    printf("Victim> Ahaha, i just trying to deanon you, %s :)\n\n", name);
    fflush(stdout);
    sleep(1);

    printf("\t(I Manage to get part of valuable data. What is it?) %p\n", (void*)&name);
    fflush(stdout);
    printf("\t(Continue dialog...)\n\n");
    fflush(stdout);
    sleep(1);

    printf("Victim> Okay, I'm a little busy, if you want to say anything else besides name, do it quick\n");
    fflush(stdout);
    printf("Me> ");
    fflush(stdout);

    gets(name);
    sleep(1);

    printf("[Victim disconnected from secret chat]\n");
    fflush(stdout);
    sleep(1);
}

int main(int argc, char *argv[]){

    printf("I claimed a contract to investigate and hack person. Let's try some social engineering...\n");
    fflush(stdout);
    sleep(4);

    printf("[Hacker connected to secret chat]\n");
    fflush(stdout);
    
    chatting();

    printf("Unfortunately, i cannot gain access to his computer. Let's try another time...\n");
    fflush(stdout);
    sleep(3);

    printf("[Hacker leaved from secret chat]");
    fflush(stdout);

    return 0;
}

