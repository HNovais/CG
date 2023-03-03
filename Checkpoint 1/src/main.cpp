#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <string>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include "rapidxml.hpp"
#include "rapidxml_utils.hpp"
#include "rapidxml_print.hpp"

using namespace rapidxml;

float alpha = 5.0f;
float beta = 0.0f;

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
    glViewport(0, 0, w, h);

	// Set perspective
	gluPerspective(45.0f ,ratio, 1.0f ,1000.0f);

	// return to the model view matrix mode
	glMatrixMode(GL_MODELVIEW);
}

void drawShape() {
	// Read the file and store the coordinates in a vector
	std::ifstream infile("D:/Universidade/CG/CG/Checkpoint 1/src/cone.3d");
	if (!infile) {
		std::cerr << "Error opening file" << std::endl;
		return;
	}

	std::vector<float> coords;
	float x, y, z;
	while (infile >> x >> y >> z) {
		coords.push_back(x);
		coords.push_back(y);
		coords.push_back(z);
	}

	std::cout << "Coords size: " << coords.size() << std::endl;

	// Print the coordinates to the console
	for (int i = 0; i < coords.size(); i += 3) {
		std::cout << "x = " << coords[i] << ", y = " << coords[i + 1] << ", z = " << coords[i + 2] << std::endl;
	}

	// Draw the triangle
	glBegin(GL_TRIANGLES);
		for (int i = 0; i < coords.size(); i += 9) {
			glVertex3f(coords[i], coords[i + 1], coords[i + 2]);
			glVertex3f(coords[i + 3], coords[i + 4], coords[i + 5]);
			glVertex3f(coords[i + 6], coords[i + 7], coords[i + 8]);
		}
	glEnd();
}

void renderScene(void) {

	// clear buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// set the camera
	glLoadIdentity();

	float camX = cos(beta) * sin(alpha);
	float camZ = cos(beta) * cos(alpha);
	gluLookAt(camX * 5, sin(beta) * 5, camZ * 5,
		      0.0,0.0,0.0,
			  0.0f,1.0f,0.0f);

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
	file<> xmlFile("configuration.xml");

	// Parse the XML file
	xml_document<> doc;
	doc.parse<0>(xmlFile.data());

	// Get the root node
	xml_node<>* rootNode = doc.first_node("world");

	// Get the window node and its attributes
	xml_node<>* windowNode = rootNode->first_node("window");
	std::string width = windowNode->first_attribute("width")->value();
	std::string height = windowNode->first_attribute("height")->value();

	// Get the camera node and its children
	xml_node<>* cameraNode = rootNode->first_node("camera");
	xml_node<>* positionNode = cameraNode->first_node("position");
	xml_node<>* lookAtNode = cameraNode->first_node("lookAt");
	xml_node<>* upNode = cameraNode->first_node("up");
	xml_node<>* projectionNode = cameraNode->first_node("projection");
	std::string x = positionNode->first_attribute("x")->value();
	std::string y = positionNode->first_attribute("y")->value();
	std::string z = positionNode->first_attribute("z")->value();
	std::string fov = projectionNode->first_attribute("fov")->value();
	std::string near = projectionNode->first_attribute("near")->value();
	std::string far = projectionNode->first_attribute("far")->value();

	// Get the group node and its child nodes
	xml_node<>* groupNode = rootNode->first_node("group");
	xml_node<>* modelsNode = groupNode->first_node("models");
	xml_node<>* modelNode = modelsNode->first_node("model");
	while (modelNode != NULL)
	{
		std::string file = modelNode->first_attribute("file")->value();
		std::cout << "Model file: " << file << std::endl;
		modelNode = modelNode->next_sibling("model");
	}
}

int main(int argc, char **argv) {

	//loadXML();

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(800,800);
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
