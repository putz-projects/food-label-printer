// Assumes the breakout board's LC has been modified to
// read INDALA at 125 kHz.

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_PN532.h>

#define PN532_IRQ   (2)
#define PN532_RESET (3)

Adafruit_PN532 nfc(PN532_IRQ, PN532_RESET);

void setup(void) {
  Serial.begin(9600);

  nfc.begin();
  
  // configure board to read RFID tags
  nfc.SAMConfig();
}


void loop(void) {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };
  uint8_t uidLength;

  // The indala card will return some static stuff that is 7 bytes. Those 7 bytes are enough
  // to be a UUID for our simple purposes. I don't want to include decryption stuff here since
  // we don't really need it.
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  
  if (success) {
    nfc.PrintHex(uid, uidLength);
    Serial.print("\n");
  }
}

