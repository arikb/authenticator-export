#Google Authenticator Generic Export Utility

This utility will read a "databases" file from the Google Authenticator
application folder on an Android phone.

Yes, you have to be able to read the file. Yes, you have to be root for that.

It then iterates over the accounts in the authenticator database and outputs QR
codes into the console with enough information in them to scan into another
OATH application (even Google Authenticator itself).

The QR codes show up as curses graphics directly in the text console. Maximise
the window so it scans better.

The command line parameter is the database file.

No guarantees here, it worked for me.

Please note the prerequisites file.
