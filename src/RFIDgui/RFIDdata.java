/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package RFIDgui;

import java.util.Objects;

/**
 *
 * @author ross
 */
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
