bool sent = false;

void setup() {
	Serial.begin(9600);
	pinMode(2, INPUT_PULLUP);
	pinMode(3, INPUT_PULLUP);
	pinMode(4, INPUT_PULLUP);
	pinMode(5, INPUT_PULLUP);
	pinMode(6, INPUT_PULLUP);
	pinMode(7, INPUT_PULLUP);
	pinMode(8, INPUT_PULLUP);

}


void loop() {
	if (!digitalRead(2)) {
		if (!sent) {
			Serial.println("On");
		}
		sent = true;
	} else if (!digitalRead(3)) {
		if (!sent) {
			Serial.println("Off");
		}
		sent = true;
	} else if (!digitalRead(4)) {
		if (!sent) {
			Serial.println("Shutdown");
		}
		sent = true;
	} else if (!digitalRead(5)) {
		if (!sent) {
			Serial.println("Kinect");
		}
		sent = true;
	} else if (!digitalRead(6)) {
		if (!sent) {
			Serial.println("Projector");
		}
		sent = true;
	} else if (!digitalRead(7)) {
		if (!sent) {
			Serial.println("Capture");
		}
		sent = true;
	} else if (!digitalRead(8)) {
		if (!sent) {
			Serial.println("ResetBG");
		}
		sent = true;
	} else {
		sent = false;
	}
	delay(10);
}
