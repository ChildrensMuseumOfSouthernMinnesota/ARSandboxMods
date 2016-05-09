bool sent = false;

void setup() {
	Serial.begin(9600);
	pinMode(8, INPUT_PULLUP);
	pinMode(9, INPUT_PULLUP);
	pinMode(10, INPUT_PULLUP);
	pinMode(11, INPUT_PULLUP);
}


void loop() {
	if (!digitalRead(8)) {
		if (!sent) {
			Serial.println("On");
		}
		sent = true;
	} else if (!digitalRead(9)) {
		if (!sent) {
			Serial.println("Off");
		}
		sent = true;
	} else if (!digitalRead(10)) {
		if (!sent) {
			Serial.println("Shutdown");
		}
		sent = true;
	} else if (!digitalRead(11)) {
		if (!sent) {
			Serial.println("Kinect");
		}
		sent = true;
	sent = true;
	} else {
		sent = false;
	}
	delay(10);
}