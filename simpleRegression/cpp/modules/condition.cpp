#include "condition.h"

#include <string>

struct Condition::dataFrame
{
	std::string firstColumn, secondColumn;
	float firstColumn [], secondColumn [];
};

Condition::Condition()(std::string firstColumn, std::string secondColumn, float firstColumn [], float secondColumn [])
	                        :predictor{ firstColumn }, predictions { secondColumn }, predoctorValues { firstColumn }, predictionValues { secondColumns } {}

float Condition::Check()
{

}

					
