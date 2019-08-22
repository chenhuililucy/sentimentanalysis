<?php
function fixBrokenUTF8($contents) {
    static $replacement = chr(0xEF) . chr(0xBF) . chr(0xBD);
    $expectingNewChar = true;
    $expectedLength = 0;
    $expectedIndex = 0;
    $i = 0;
    $out = "";
    while ($i < strlen($contents)) {
        $byte = ord($contents[$i]);
        // Start of a new character?
        if ($expectingNewChar) {
            // 1-byte ASCII chars, append to output
            if ($byte < 0x80) {
                $out .= $contents[$i];
            }
            // First byte >= 0xF0 means a 4-byte char
            elseif ($byte >= 0xF0) {
                $expectingNewChar = false;
                $expectedLength = 4;
                $expectedIndex = 2;
            }
            // First byte >= 0xE0 means a 3-byte char
            elseif ($byte >= 0xE0) {
                $expectingNewChar = false;
                $expectedLength = 3;
                $expectedIndex = 2;
            }
            // First byte >= 0xC0 means a 2-byte char
            elseif ($byte >= 0xC0) {
                $expectingNewChar = false;
                $expectedLength = 2;
                $expectedIndex = 2;
            }
        }
        // Not the start of a new char, but expecting
        // one of the bytes in a multibyte char
        else {
            // Subsequent bytes in a multibyte char have
            // to be between 0x80 and 0xC0. If it's not
            // then something is corrupt, so add the replacement
            // char to the output and look for a new char
            if (! (($byte >= 0x80) && ($byte < 0xC0))) {
                $out .= $replacement;
                $expectingNewChar = true;
                // This prevents $i++ at the end of the loop,
                // since this "corrupt" byte could be the start
                // of a new character
                continue;
            } else {
                // A valid byte, but we haven't gotten as many
                // bytes for this char yet as we need
                if ($expectedIndex < $expectedLength) {
                    $expectedIndex++;
                }
                // Gotten all the bytes for the valid multibyte char,
                // put them in the output and expect a new character
                // next.
                else {
                    $out .= substr($contents, $i - $expectedLength + 1,
                                   $expectedLength);
                    $expectingNewChar = true;
                }
            }
        }
        // Advance to the next byte
        $i++;
    }
    return $out;
}