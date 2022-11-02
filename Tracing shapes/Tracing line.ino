#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
double theta1[100]={68.7, 68.2, 67.8, 67.3, 66.9, 66.5, 66.1, 65.7, 
65.3, 64.9, 64.5, 64.2, 63.8, 63.5, 63.2, 62.9, 62.6, 62.3, 
62.0000000000000, 61.7, 61.4, 61.1, 60.9, 60.6, 60.4, 60.1, 59.9, 
59.7, 59.5, 59.3, 59.0000000000000, 58.8, 58.7, 58.5, 58.3, 58.1, 
57.9, 57.8, 57.6, 57.5, 57.3, 57.2, 57.0000000000000, 56.9, 56.8, 
56.7, 56.6, 56.4, 56.3, 56.2, 56.2, 56.1, 56.0000000000000, 55.9, 
55.8, 55.8, 55.7, 55.6, 55.6, 55.5, 55.5, 55.5, 55.4, 55.4, 55.4, 
55.3, 55.3, 55.3, 55.3, 55.3, 55.3, 55.3, 55.3, 55.3, 55.4, 55.4, 
55.4, 55.4, 55.5, 55.5, 55.6, 55.6, 55.7, 55.7, 55.8, 55.9, 55.9, 
56.0000000000000, 56.1, 56.2, 56.3, 56.3, 56.4, 56.5, 56.6, 56.8, 
56.9, 57.0000000000000, 57.1, 57.2};


double theta2[100]={130.2, 131.1, 131.9, 132.7, 133.5, 134.2, n
135.000000000000, 135.7, 136.4, 137.1, 137.7, 138.4, 
139.000000000000, 139.6, 140.2, 140.7, 141.3, 141.8, 142.4, 142.9, 
143.4, 143.8, 144.3, 144.8, 145.2, 145.6, 146.1, 146.5, 146.9, 
147.2, 147.6, 148.000000000000, 148.3, 148.6, 149.000000000000, 
149.3, 149.6, 149.9, 150.2, 150.4, 150.7, 150.9, 151.2, 151.4, 
151.6, 151.8, 152.000000000000, 152.2, 152.4, 152.6, 152.7, 152.9, 
153.000000000000, 153.2, 153.3, 153.4, 153.5, 153.6, 153.7, 153.7, 
153.8, 153.9, 153.9, 154.000000000000, 154.000000000000, 
154.000000000000, 154.000000000000, 154.000000000000, 
154.000000000000, 154.000000000000, 154.000000000000, 153.9, 153.9, 
153.8, 153.7, 153.7, 153.6, 153.5, 153.4, 153.3, 153.1, 
153.000000000000, 152.9, 152.7, 152.6, 152.4, 152.2, 
152.000000000000, 151.8, 151.6, 151.4, 151.1, 150.9, 150.6, 150.4, 
150.1, 149.8, 149.5, 149.2, 148.9};


double theta3[100]={70.3, 71.2, 72.2, 73.1, 74.1, 75.0000000000000, 
75.9, 76.8, 77.7, 78.6, 79.4, 80.3, 81.1, 82.0000000000000, 82.8, 
83.7, 84.5, 85.3, 86.1, 86.9, 87.7, 88.5, 89.3, 90.1, 90.8, 91.6, 
92.4, 93.1, 93.9, 94.6, 95.3, 96.1, 96.8, 97.5, 98.3, 
99.0000000000000, 99.7, 100.4, 101.1, 101.8, 102.5, 103.2, 103.8, 
104.5, 105.2, 105.9, 106.5, 107.2, 107.8, 108.5, 109.1, 109.8, 
110.4, 111.000000000000, 111.7, 112.3, 112.9, 113.5, 114.1, 114.7, 
115.3, 115.9, 116.5, 117.1, 117.7, 118.3, 118.8, 119.4, 
120.000000000000, 120.5, 121.1, 121.6, 122.2, 122.7, 123.2, 123.7, 
124.3, 124.8, 125.3, 125.8, 126.3, 126.8, 127.3, 127.8, 128.2, 
128.7, 129.2, 129.6, 130.1, 130.5, 131.000000000000, 131.4, 131.8, 
132.3, 132.7, 133.1, 133.5, 133.9, 134.3, 134.7};


void setup()
{
 servo1.attach(4);
 servo2.attach(5);
 servo3.attach(6);
 servo1.write(theta1[0]);
 servo2.write(theta2[0]);
 servo3.write(theta3[0]);
 delay(1000);
 for(int i=0;i<s100;i++)
 {
 servo1.write(theta1[i]);
 servo2.write(theta2[i]);
 servo3.write(theta3[i]);
 delay(100);
 // Serial.println(theta1[i]);
 // Serial.println(theta2[i]);
 // Serial.println(theta3[i]);
 }
 delay(3000);
}
void loop()
{
 servo1.write(90);
 servo2.write(90);
 servo3.write(90);
}