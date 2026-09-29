#include <stdio.h>

#define MAX_STUDENTS   50
#define MAX_COMPLAINTS 50
#define ROOMS          5
#define FEE            11000      /* hostel 8000 + mess 3000 */

struct Student {
    int  id;
    char name[50];
    char phone[15];
    int  room;         /* 0 means no room */
    int  checkedIn;    /* 0 = no, 1 = yes */
    int  paid;         /* fee paid so far */
};

struct Complaint {
    int  studentId;
    char text[100];
    int  resolved;     /* 0 = pending, 1 = resolved */
};

struct Student   students[MAX_STUDENTS];
struct Complaint complaints[MAX_COMPLAINTS];
int studentCount = 0, complaintCount = 0;

/* rooms are numbered 1 to 5, so index 0 is not used */
int capacity[ROOMS + 1] = {0, 4, 2, 4, 3, 2};
int occupied[ROOMS + 1] = {0};

/* ---------- helper functions ---------- */

/* returns the position of the student in the array, or -1 if not found */
int findStudent(int id) {
    int i;
    for (i = 0; i < studentCount; i++)
        if (students[i].id == id) return i;
    return -1;
}

/* asks for a student ID and returns that student's position (or -1) */
int askStudent() {
    int id, i;
    printf("Enter student ID: ");
    scanf("%d", &id);
    i = findStudent(id);
    if (i == -1) printf("Student not found!\n");
    return i;
}

/* ---------- 1. student registration ---------- */
void registerStudent() {
    struct Student s;
    if (studentCount == MAX_STUDENTS) { printf("Student list is full!\n"); return; }
    printf("Enter student ID: ");
    scanf("%d", &s.id);
    if (findStudent(s.id) != -1) { printf("This ID already exists!\n"); return; }
    printf("Name: ");
    scanf(" %49[^\n]", s.name);
    printf("Phone: ");
    scanf("%14s", s.phone);
    s.room = 0;
    s.checkedIn = 0;
    s.paid = 0;
    students[studentCount] = s;        /* copy the filled form into the register */
    studentCount++;
    printf("Student registered successfully!\n");
}

/* ---------- 2. rooms ---------- */
void showVacancy() {
    int r, totalBeds = 0, usedBeds = 0;
    for (r = 1; r <= ROOMS; r++) {
        printf("Room %d : %d/%d occupied\n", r, occupied[r], capacity[r]);
        totalBeds += capacity[r];
        usedBeds += occupied[r];
    }
    printf("Available beds: %d of %d\n", totalBeds - usedBeds, totalBeds);
}

void allocateRoom() {
    int s, r;
    s = askStudent();
    if (s == -1) return;
    if (students[s].room != 0) { printf("Student already has a room!\n"); return; }
    showVacancy();
    printf("Enter room number: ");
    scanf("%d", &r);
    if (r < 1 || r > ROOMS)              printf("No such room!\n");
    else if (occupied[r] == capacity[r]) printf("Room is FULL!\n");
    else {
        students[s].room = r;
        occupied[r]++;
        printf("Room %d allocated to %s.\n", r, students[s].name);
    }
}

/* ---------- 3. fee ---------- */
void payFee() {
    int s, amount, balance;
    s = askStudent();
    if (s == -1) return;
    balance = FEE - students[s].paid;
    printf("Total: Rs.%d | Paid: Rs.%d | Balance: Rs.%d\n", FEE, students[s].paid, balance);
    if (balance == 0) { printf("No pending fee.\n"); return; }
    printf("Enter amount to pay: ");
    scanf("%d", &amount);
    if (amount <= 0 || amount > balance) printf("Invalid amount!\n");
    else {
        students[s].paid += amount;
        printf("Payment successful! Balance now: Rs.%d\n", balance - amount);
    }
}


int main() {
    int choice;
    do {
        printf("\n===== HOSTEL MANAGEMENT SYSTEM =====\n");
        printf("1. Register Student\n2. Allocate Room\n3. Room Vacancy\n");
        printf("4. Pay Fee\n5. Register Complaint\n6. View Complaints\n");
        printf("7. Resolve Complaint\n8. Check-in\n9. Check-out\n");
        printf("10. Search Student\n11. Display All Students\n0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:  registerStudent();  break;
            case 2:  allocateRoom();     break;
            case 3:  showVacancy();      break;
            case 4:  payFee();           break;

            case 0:  printf("Goodbye!\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 0);
    return 0;
}