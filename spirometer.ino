const float ADC_mV = 4.8828125;       // convesion multiplier from Arduino ADC value to voltage in mV
const float SensorOffset = 200.0;     // in mV taken from datasheet
const float sensitivity = 4.413;      // in mV/mmH2O taken from datasheet
const float mmh2O_cmH2O = 10;         // divide by this figure to convert mmH2O to cmH2O
const float mmh2O_kpa = 0.00981;      // convesion multiplier from mmH2O to kPa
int count = 0;
int sum = 0;

float pi = 3.14;
float q = 0;
float d1 = 1.8;
float d2 = 1.3;
float fd = 1.2;
float dp = 0;
float area_d1 = 2.5446;
float area_d2 = 1.3273;
float num = 0;
float denom = 0;
float volume = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  delay(100);
//  count++;
    
  
  // ((sensorValue in mV -sensorOffset)/sensitivity in mV/mmH2O)*kPa conversion constant
  float sensorValue = ((analogRead(A0) * ADC_mV - SensorOffset) / sensitivity * mmh2O_kpa);     // result in kPa
    dp = sensorValue*1000;
    num = 2*dp;
    denom = fd*(pow(area_d1/area_d2, 2)-1);
    q = area_d1 * sqrt(num/denom);
    // q = area_d1*(sqrt((2*dp)/fd*(pow(area_d1/area_d2, 2))-1));
//    Serial.print(-0.1); // To freeze the lower limit
//  Serial.print(" ");
//  Serial.print(1); // To freeze the upper limit
//  Serial.print(" ");
    Serial.println(sensorValue);
//    if(sensorValue > 0.20){
//      count++;
//      if(count == 10){
//        count=0;
//        Serial.println("------");
//        volume = 0;
//        }

//    volume += q*0.1;
//    Serial.println("Volume in litres : ");
//    Serial.println(volume);
//    }
//    Serial.print("%.4f (litres):");
//    Serial.println(q/10);
}