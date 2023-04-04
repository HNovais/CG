#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <io.h>
#include <direct.h>
#include <structs.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include "rapidxml.hpp"
#include "rapidxml_utils.hpp"
#include "rapidxml_print.hpp"


using namespace rapidxml;
using namespace std;

XML_Struct estrutura;

float alpha = 0.0f;
float beta = 0.0f;

int width = 0;
int height = 0;

float fov = 0.0f;
float near = 0.0f;
float far = 0.0f;

std::vector<float> cameraValues;
std::vector<std::vector<float>> modelsCoords;

std::vector<std::vector<float>> translateValues;
std::vector<std::vector<float>> rotateValues;
std::vector<std::vector<float>> scaleValues;

std::vector<int> xmlValues;

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


void drawShape(int i) {
	std::vector<float> coords = modelsCoords[i];

	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

	glBegin(GL_TRIANGLES);
	for (int j = 0; j < coords.size(); j += 9) {
		glVertex3f(coords[j], coords[j + 1], coords[j + 2]);
		glVertex3f(coords[j + 3], coords[j + 4], coords[j + 5]);
		glVertex3f(coords[j + 6], coords[j + 7], coords[j + 8]);
	}
	glEnd();
}

void drawShape2(Model model) {
	vector<float> coords = model.points;

	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

	glBegin(GL_TRIANGLES);
	for (int j = 0; j < coords.size(); j += 9) {
		glVertex3f(coords[j], coords[j + 1], coords[j + 2]);
		glVertex3f(coords[j + 3], coords[j + 4], coords[j + 5]);
		glVertex3f(coords[j + 6], coords[j + 7], coords[j + 8]);
	}
	glEnd();
}


void readValues() {
	int models = 0;
	int transforms = 0;
	int groups = 1;

	//glPushMatrix();

	for (int i = 0; i < xmlValues.size(); i++) {
		int action = xmlValues[i];

		if (action == 0) {
			glPushMatrix();
			groups += 1;
		}

		else if (action == 1) {
			std::vector<float> tran = translateValues[transforms];/*
			std::vector<float> rot = rotateValues[transforms];
			std::vector<float> scl = scaleValues[transforms];
			*/
			glTranslatef(tran[0], tran[1], tran[2]);
			//glRotatef(rot[0], rot[1], rot[2], rot[3]);
			//glScalef(scl[0], scl[1], scl[2]);

			transforms += 1;
		}

		else if (action == 2) {
			drawShape(models);
			models += 1;
		}
	}

	for (int j = 0; j < groups; j++) {
		glPopMatrix();
	}
}

void transformation(Transform transform) {
	if (transform.type=="translate"){
		glTranslated(transform.x, transform.y, transform.z);
	}
	else if (transform.type == "rotate") {
		glRotated(transform.angle,transform.x, transform.y, transform.z);
	}
	else if (transform.type == "scale") {
		glScaled(transform.x, transform.y, transform.z);
	}
}

void processgroup(Group group) {
	glPushMatrix();

	for (int i;i < group.transforms.size();i++) {
		transformation(group.transforms[i]);
	}

	for (int i;i < group.models.size();i++) {
		drawShape2(group.models[i]);
	}

	for (int i;i < group.groups.size();i++) {
		processgroup(group.groups[i]);
	}

	glPopMatrix();
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
	/*
	gluLookAt(x, y, z,
		      lookAtX,lookAtY,lookAtZ,
			  upX,upY,upZ);
	*/

	gluLookAt(estrutura.camera.position.x, estrutura.camera.position.y, estrutura.camera.position.z,
		estrutura.camera.lookAt.x, estrutura.camera.lookAt.y, estrutura.camera.lookAt.z,
		estrutura.camera.up.x, estrutura.camera.up.y, estrutura.camera.up.z);

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

	//processgroup(estrutura.group);
	readValues();
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


void loadXML(XML_Struct& estrutura) {

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

	estrutura.window.width= stoi(windowNode->first_attribute("width")->value());
	estrutura.window.height = stoi(windowNode->first_attribute("height")->value());

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
	estrutura.camera.position.x = stof(positionNode->first_attribute("x")->value());
	estrutura.camera.position.y = stof(positionNode->first_attribute("y")->value());
	estrutura.camera.position.z = stof(positionNode->first_attribute("z")->value());

	cameraValues.push_back(std::stof(lookAtNode->first_attribute("x")->value()));
	cameraValues.push_back(std::stof(lookAtNode->first_attribute("y")->value()));
	cameraValues.push_back(std::stof(lookAtNode->first_attribute("z")->value()));
	estrutura.camera.lookAt.x = stof(lookAtNode->first_attribute("x")->value());
	estrutura.camera.lookAt.y = stof(lookAtNode->first_attribute("y")->value());
	estrutura.camera.lookAt.z = stof(lookAtNode->first_attribute("z")->value());

	cameraValues.push_back(std::stof(upNode->first_attribute("x")->value()));
	cameraValues.push_back(std::stof(upNode->first_attribute("y")->value()));
	cameraValues.push_back(std::stof(upNode->first_attribute("z")->value()));
	estrutura.camera.up.x = stof(upNode->first_attribute("x")->value());
	estrutura.camera.up.y = stof(upNode->first_attribute("y")->value());
	estrutura.camera.up.z = stof(upNode->first_attribute("z")->value());

	fov = std::stof(projectionNode->first_attribute("fov")->value());
	near = std::stof(projectionNode->first_attribute("near")->value());
	far = std::stof(projectionNode->first_attribute("far")->value());
	std::cout << "Camera Projection: " << "FOV: " << fov << " Near: " << near << " Far: " << far << std::endl;
	estrutura.camera.projection.far= stof(projectionNode->first_attribute("fov")->value());;
	estrutura.camera.projection.fov= stof(projectionNode->first_attribute("far")->value());;
	estrutura.camera.projection.near=stof(projectionNode->first_attribute("near")->value());

	// Get the group node and its child nodes

	xml_node<>* groupNode = rootNode->first_node("group");

	while (groupNode != NULL) {
		xmlValues.push_back(0);

		xml_node<>* transformNode = groupNode->first_node("transform");
		
		if (transformNode != NULL) {
			xml_node<>* translateNode = transformNode->first_node("translate");
			xml_node<>* rotateNode = transformNode->first_node("rotate");
			xml_node<>* scaleNode = transformNode->first_node("scale");

			float a = 0.0f;
			float x = 0.0f;
			float y = 0.0f;
			float z = 0.0f;

			std::vector<float> coords;

			if (translateNode != NULL) {
				x = std::stof(translateNode->first_attribute("x")->value());
				y = std::stof(translateNode->first_attribute("y")->value());
				z = std::stof(translateNode->first_attribute("z")->value());
				std::cout << "Translation: " << "X: " << x << " Y: " << y << " Z: " << z << std::endl;
				coords.push_back(x);
				coords.push_back(y);
				coords.push_back(z);

				translateValues.push_back(coords);
			}
			else {
				x = 0;
				y = 0;
				z = 0;

				coords.push_back(x);
				coords.push_back(y);
				coords.push_back(z);

				translateValues.push_back(coords);
			}

			std::vector<float> rt;

			if (rotateNode != NULL) {
				a = std::stof(rotateNode->first_attribute("angle")->value());
				x = std::stof(rotateNode->first_attribute("x")->value());
				y = std::stof(rotateNode->first_attribute("y")->value());
				z = std::stof(rotateNode->first_attribute("z")->value());

				rt.push_back(a);
				rt.push_back(x);
				rt.push_back(y);
				rt.push_back(z);

				rotateValues.push_back(rt);
			}
			else {
				a = 0.0f;
				x = 0.0f;
				y = 0.0f;
				z = 0.0f;

				rt.push_back(a);
				rt.push_back(x);
				rt.push_back(y);
				rt.push_back(z);

				rotateValues.push_back(rt);
			}

			std::vector<float> sc;

			if (scaleNode != NULL) {
				x = std::stof(scaleNode->first_attribute("x")->value());
				y = std::stof(scaleNode->first_attribute("y")->value());
				z = std::stof(scaleNode->first_attribute("z")->value());

				sc.push_back(x);
				sc.push_back(y);
				sc.push_back(z);

				scaleValues.push_back(sc);
			}
			else {
				x = 0.0f;
				y = 0.0f;
				z = 0.0f;

				sc.push_back(x);
				sc.push_back(y);
				sc.push_back(z);

				scaleValues.push_back(sc);
			}
			
			xmlValues.push_back(1);
		}

		xml_node<>* modelsNode = groupNode->first_node("models");
		
		if (modelsNode != NULL) {
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

			xmlValues.push_back(2);
		}

		xml_node<>* nextNode = groupNode->first_node("group");

		groupNode = nextNode;
	}
}

int main(int argc, char **argv) {

	loadXML(estrutura);

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(width,height);
	glutCreateWindow("grupo31");
		
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
