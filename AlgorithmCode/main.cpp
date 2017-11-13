//
//  main.cpp
//  DecisionAlg
//
//  Created by Sydnee Mizuno on 9/11/17.
//  Copyright © 2017 Sydnee Mizuno. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {

    bool human = 0;
    
    bool light = 0;
    int ambientLight = 0;
    int setLight = 0;

    bool blinds = 0;
    int outTemp = 0;
    int setTemp = 0;
    
    bool window = 0;
    bool airCond = 0;
    bool heater = 0;
    bool coolingOn = 0;
    bool heatingOn = 0;
    bool ecoMode = 0;
    int ambientTemp = 0;
    
    
    /**********************************************************************/
    // Blinds
    if (human == 1)
    {
        if(blinds == 1)
        {
            blinds = 1;
        }
        else
        {
            if(ambientLight >= setLight)
            {
                blinds = 0;
            }
            else
            {
                blinds = 1;
            }
        }
    }
    else
    {
        if(blinds == 1)
        {
            if(outTemp > setTemp)
            {
                blinds = 0;
            }
            else
            {
                blinds = 1;
            }
        }
        else
        {
            blinds = 0;
        }
    }
    
    /**********************************************************************/
    // Lights
    if (human == 1)
    {
        if (ambientLight < setLight)
        {
            light = 1;
        }
    }
    else
    {
        light = 0;
    }

    /**********************************************************************/
    // HVAC
    // Cooling
    if (coolingOn == 1)
    {
        if (ambientTemp > setTemp)
        {
            if (outTemp > ambientTemp)
            {
                if (ecoMode == 0)
                {
                    window = 0;
                    airCond = 1;
                }
                else
                {
                    window = 0;
                    airCond = 1;
                }
            }
            else // outTemp < ambientTemp
            {
                if (outTemp < setTemp)
                {
                    if (ecoMode == 0)
                    {
                        window = 1;
                        airCond = 0;
                    }
                    else
                    {
                        window = 1;
                        airCond = 0;
                    }
                }
                else // outTemp > setTemp
                {
                    if (ecoMode == 0)
                    {
                        window = 1;
                        airCond = 1;
                    }
                    else
                    {
                        window = 1;
                        airCond = 0;
                    }
                }
            }
        }
        else // ambientTemp < setTemp
        {
            window = 0;
            airCond = 0;
        }
    }
    
    /**********************************************************************/
    // Heating
    if (heatingOn == 1)
    {
        if (ambientTemp < setTemp)
        {
            if (outTemp < ambientTemp)
            {
                if (ecoMode == 0)
                {
                    window = 0;
                    heater = 1;
                }
                else
                {
                    window = 0;
                    heater = 1;
                }
            }
            else // outTemp > ambientTemp
            {
                if (outTemp > setTemp)
                {
                    if (ecoMode == 0)
                    {
                        window = 1;
                        heater = 0;
                    }
                    else
                    {
                        window = 1;
                        heater = 0;
                    }
                }
                else // outTemp < setTemp
                {
                    if (ecoMode == 0)
                    {
                        window = 1;
                        heater = 1;
                    }
                    else
                    {
                        window = 1;
                        heater = 0;
                    }
                }
            }
        }
        else // ambientTemp > setTemp
        {
            window = 0;
            heater = 0;
        }
    }

    

    return 0;
}
