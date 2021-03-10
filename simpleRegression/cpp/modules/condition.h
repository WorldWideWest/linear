#ifndef _CONDITION_H_
#define _CONDITION_H_
#pragma once

#include <string>

class Condition
{
	public:
		std::string predictor, predictions;
		float predictorValues [], predictionsValues [];
		
		Condition(std::string firstColumn, std::string secondColumn, float firstColumn [], float secondColumn []);

		float Check();


}

#endif
