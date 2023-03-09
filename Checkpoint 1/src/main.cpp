#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <string>
#include <io.h>
#include <direct.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include "rapidxml.hpp"
#include "rapidxml_utils.hpp"
#include "rapidxml_print.hpp"

using namespace rapidxml;

float alpha = 0.0f;
float beta = 0.0f;

int width = 0;
int height = 0;

float fov = 0.0f;
float near = 0.0f;
float far = 0.0f;

std::vector<float> cameraValues;
std::vector<std::vector<float>> modelsCoords;

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window with zero width).
	if(h == 0)
		h = 1;

	// compute window's aspect ratio 
	float ratio = w * 1.0 / h;

	// Set the projection matrix as current
	glMatrixMode(GL_PROJECTION);
	// Load Identity Matrix
	glLoadIdentity();
	
	// Set the viewport to be the entire window
	glViewport(0, 0, width, height);

	gluPerspective(fov, width / height, near, far);

	// return to the model view matrix mode
	glMatrixMode(GL_MODELVIEW);
}


void drawShape() {
	for (int i = 0; i < modelsCoords.size(); i++) {
		std::vector<float> coords = modelsCoords[i];

		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
		// Draw the model
		glBegin(GL_TRIANGLES);
		for (int j = 0; j < coords.size(); j += 9) {
			glVertex3f(coords[j], coords[j + 1], coords[j + 2]);
			glVertex3f(coords[j + 3], coords[j + 4], coords[j + 5]);
			glVertex3f(coords[j + 6], coords[j + 7], coords[j + 8]);
		}
		glEnd();
	}
}


void renderScene() {

	float x = cameraValues[0];
	float y = cameraValues[1];
	float z = cameraValues[2];
	float lookAtX = cameraValues[3];
	float lookAtY = cameraValues[4];
	float lookAtZ = cameraValues[5];
	float upX = cameraValues[6];
	float upY = cameraValues[7];
	float upZ = cameraValues[8];

	// clear buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// set the camera
	glLoadIdentity();
	
	float camX = cos(beta) * sin(alpha);
	float camZ = cos(beta) * cos(alpha);
	gluLookAt(camX + x, sin(beta) + y, camZ + z,
		      lookAtX,lookAtY,lookAtZ,
			  upX,upY,upZ);

	

	glBegin(GL_LINES);
		// X axis in red
		glColor3f(1.0f, 0.0f, 0.0f);
		glVertex3f(
			-100.0f, 0.0f, 0.0f);
		glVertex3f(100.0f, 0.0f, 0.0f);
		// Y Axis in Green
		glColor3f(0.0f, 1.0f, 0.0f);
		glVertex3f(0.0f,
			-100.0f, 0.0f);
		glVertex3f(0.0f, 100.0f, 0.0f);
		// Z Axis in Blue
		glColor3f(0.0f, 0.0f, 1.0f);
		glVertex3f(0.0f, 0.0f,
			-100.0f);
		glVertex3f(0.0f, 0.0f, 100.0f);
	glEnd();

	glColor3f(1.0f, 1.0f, 1.0f);
	drawShape();

	// End of frame
	glutSwapBuffers();
}


void processKeys(unsigned char key, int xx, int yy) {
	switch (key) {
	case 'a':
	case 'A':
		alpha -= 0.1f;
		break;
	case 'd':
	case 'D':
		alpha += 0.1f;
		break;
	case 'w':
	case 'W':
		if(beta <= 1.5f)
			beta += 0.1f;
		break;
	case 's':
	case 'S':
		if(beta >= -1.5f)
			beta -= 0.1f;
		break;
	default:
		break;
	}
	glutPostRedisplay();

}


void loadXML() {

	// Load the XML file
	file<> xmlFile("../src/configuration.xml");

	// Parse the XML file
	xml_document<> doc;
	doc.parse<0>(xmlFile.data());

	// Get the root node
	xml_node<>* rootNode = doc.first_node("world");

	// Get the window node and its attributes
	xml_node<>* windowNode = rootNode->first_node("window");
	width = std::stoi(windowNode->first_attribute("width")->value());
	height = std::stoi(windowNode->first_attribute("height")->value());

	// Get the camera node and its children
	xml_node<>* cameraNode = rootNode->first_node("camera");
	xml_node<>* positionNode = cameraNode->first_node("position");
	xml_node<>* lookAtNode = cameraNode->first_node("lookAt");
	xml_node<>* upNode = cameraNode->first_node("up");
	xml_node<>* projectionNode = cameraNode->first_node("projection");

	cameraValues.push_back(std::stof(positionNode->first_attribute("x")->value()));
	cameraValues.push_back(std::stof(positionNode->first_attribute("y")->value()));
	cameraValues.push_back(std::stof(positionNode->first_attribute("z")->value()));
	std::cout << "Camera Values: " << "X: " << std::stof(positionNode->first_attribute("x")->value()) << " Y: " << std::stof(positionNode->first_attribute("y")->value()) << " Z: " << std::stof(positionNode->first_attribute("z")->value()) << std::endl;
	cameraValues.push_back(std::stof(lookAtNode->first_attribute("x")->value()));
	cameraValues.push_back(std::stof(lookAtNode->first_attribute("y")->value()));
	cameraValues.push_back(std::stof(lookAtNode->first_attribute("z")->value()));
	cameraValues.push_back(std::stof(upNode->first_attribute("x")->value()));
	cameraValues.push_back(std::stof(upNode->first_attribute("y")->value()));
	cameraValues.push_back(std::stof(upNode->first_attribute("z")->value()));
	fov = std::stof(projectionNode->first_attribute("fov")->value());
	near = std::stof(projectionNode->first_attribute("near")->value());
	far = std::stof(projectionNode->first_attribute("far")->value());
	std::cout << "Camera Projection: " << "FOV: " << fov << " Near: " << near << " Far: " << far << std::endl;

	// Get the group node and its child nodes
	xml_node<>* groupNode = rootNode->first_node("group");
	xml_node<>* modelsNode = groupNode->first_node("models");
	xml_node<>* modelNode = modelsNode->first_node("model");

	while (modelNode != NULL)
	{
		char cwd[1024];

		std::string file = modelNode->first_attribute("file")->value();

		std::vector<float> coords;
		float x, y, z;
		std::string file_path = "../src/" + file;
		std::cout << "Loading model from file: " << file_path << std::endl;

		std::ifstream infile(file_path);

		while (infile >> x >> y >> z) {
			coords.push_back(x);
			coords.push_back(y);
			coords.push_back(z);
		}

		modelsCoords.push_back(coords);

		modelNode = modelNode->next_sibling("model");
	}
}


int main(int argc, char **argv) {

	loadXML();

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(width,height);
	glutCreateWindow("ez");
		
// Required callback registry 
	glutDisplayFunc(renderScene);
	glutReshapeFunc(changeSize);
	
// Callback registration for keyboard processing
	glutKeyboardFunc(processKeys);

//  OpenGL settings
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_CULL_FACE);
	
// enter GLUT's main cycle
	glutMainLoop();
	
	return 1;
}
