# Micro-Teach Cheat Sheet: Smart Home Security System

**Topic:** Building a Motion-Activated Alarm
**Time Limit:** 5-7 Minutes for this specific demo part.

## 1. The Circuit (Memorize This)

**Components on Tinkercad:**
1.  **Arduino Uno R3**
2.  **Breadboard Small**
3.  **PIR Sensor** (The one with the white dome)
4.  **LED** (Red)
5.  **Resistor** (220 ohm - Red/Red/Brown)

**Wiring Instructions (Practice this beforehand):**
*   **PIR Sensor:**
    *   *Signal* pin  -> Arduino **Pin 2**
    *   *Power* pin   -> **5V**
    *   *Ground* pin  -> **GND**
*   **LED:**
    *   *Long leg (Anode)* -> Arduino **Pin 13**
    *   *Short leg (Cathode)* -> Resistor -> **GND**

---

## 2. The Code (Keep it Simple)

In Tinkercad, switch looking at **"Text"** mode (not Blocks) if you are comfortable, or stick to Blocks if you prefer speed. **Text is more impressive for a University Lecturer role.**

```cpp
// Define Pins
int sensorPin = 2; // The PIR Sensor
int ledPin = 13;   // The Alarm Light

void setup() {
  pinMode(sensorPin, INPUT); // Sensor sends data IN to Arduino
  pinMode(ledPin, OUTPUT);   // Arduino sends power OUT to LED
  Serial.begin(9600);        // Listen to the system
}

void loop() {
  // Read the sensor
  int status = digitalRead(sensorPin);
  
  if (status == HIGH) {
    // Motion DETECTED!
    digitalWrite(ledPin, HIGH); // Turn Light ON
    Serial.println("INTRUDER ALERT!"); 
  } else {
    // No Motion
    digitalWrite(ledPin, LOW);  // Turn Light OFF
  }
  delay(100); // Small pause for stability
}
```

---

## 3. The "Think Aloud" Script (Say this WHILE you build)

**Step 1: Introduction (10 seconds)**
> "Okay class, today we are building the core of a Smart Home Security system. We want a light to turn on automatically when someone enters the room."

**Step 2: Placing the Sensor (30 seconds)**
> "First, we need our 'eyes'. I am placing this **PIR Motion Sensor**.
> *Ask:* Does anyone know what PIR stands for? ... It stands for Passive Infrared. It detects heat energy, like body heat."

**Step 3: Wiring the Input (45 seconds)**
> "Now, I connect the Sensor Signal to **Pin 2**.
> I am defining this as an **INPUT** because the sensor gives information *to* the computer."

**Step 4: Placing the Output (30 seconds)**
> "Next, we need an output to warn us. I'm using this **Red LED**.
> *Ask:* Why do I need this Resistor here? ... Exactly, to protect the LED from burning out by limiting the current."

**Step 5: The Code Logic (60 seconds)**
> "Now let's tell the Arduino what to do.
> The logic is a simple **IF Statement**.
> *Type:* `if (digitalRead(sensorPin) == HIGH)` ...
> This translates to: 'If the sensor sees a person, THEN turn the LED HIGH (On). Else, turn it LOW (Off).'"

**Step 6: The Test (20 seconds)**
> "Let's simulate. I click 'Start Simulation'.
> Now, if I move this virtual object in front of the sensor... *Click and drag mouse*...
> **Success!** The light turns on. The security system works."

---

## 4. The Physical Transition (30 seconds)

> **[STOP SCREEN SHARE -> TURN ON CAMERA]**
>
> "So that logic works perfectly in code.
> But in the real world, we deal with physical constraints.
> *(Hold up your real Arduino and white PIR sensor)*
> Here is the physical version of that exact circuit.
> In our next lab, you will wire this yourself. You'll learn that real sensors have 'sensitivity' dials we need to adjust with a screwdriver, something the simulator doesn't always show us. That is why **Hands-On** skills are critical."
