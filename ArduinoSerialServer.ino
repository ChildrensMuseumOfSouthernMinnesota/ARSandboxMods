bool sent = false;

void setup() {
	Serial.begin(9600);
	pinMode(8, INPUT_PULLUP);
	pinMode(9, INPUT_PULLUP);
	pinMode(10, INPUT_PULLUP);
	pinMode(11, INPUT_PULLUP);
	pinMode(12, INPUT_PULLUP);
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
	} else if (!digitalRead(12)) {
		if (!sent) {
			Serial.println("Projector");
		}
		sent = true;
	} else if (!digitalRead(2)) {
		if (!sent) {
			Serial.println("Capture");
		}
		sent = true;
	} else if (!digitalRead(3)) {
		if (!sent) {
			Serial.println("ResetBG");
		}
		sent = true;
	} else {
		sent = false;
	}
	delay(10);
}
