/* MIT License
 * 
 * Copyright (c) [2016] [Ross Bunker]
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package RFIDgui;

import java.util.Objects;

public class RFIDdata {
    public String tagNumber = "-1";
    public String objectName = "Default Name";
    public String objectDescription = "Default description.";
    public boolean hasPicture = false;
    
    public RFIDdata(){ }
    
    public RFIDdata(String tagNumberIn) {
        tagNumber = tagNumberIn;
    }
    
    public RFIDdata(String tagNumberIn, String nameIn, String descriptionIn) {
        tagNumber = tagNumberIn;
        objectName = nameIn;
        objectDescription = descriptionIn;
    }
    
    public RFIDdata(String tagNumberIn, String nameIn, String descriptionIn, boolean hasPictureIn) {
        tagNumber = tagNumberIn;
        objectName = nameIn;
        objectDescription = descriptionIn;
        hasPicture = hasPictureIn;
    }
    
    @Override
    public boolean equals(Object v) {
        boolean retVal = false;

        if (v instanceof RFIDdata) {
            RFIDdata ptr = (RFIDdata) v;
            retVal = this.tagNumber.equals(ptr.tagNumber);
        }

        return retVal;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 17 * hash + Objects.hashCode(this.tagNumber);
        return hash;
    }
    
    public String getID() {
        return this.tagNumber;
    }
}
