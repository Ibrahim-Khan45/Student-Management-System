# Makefile for University Management System

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++11 -Wall -Wextra -O2

# Target executable
TARGET = ums

# Source files
SOURCES = main.cpp student.cpp exam.cpp transport.cpp

# Object files
OBJECTS = $(SOURCES:.cpp=.o)

# Default target
all: $(TARGET)

# Build the executable
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)
	@echo "Build successful! Run ./$(TARGET) to start the program."

# Compile source files to object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean build files
clean:
	rm -f $(OBJECTS) $(TARGET)
	@echo "Clean complete."

# Clean everything including data files
clean-all: clean
	rm -f students.txt exams.txt transport.txt transport_queue.txt
	@echo "All files cleaned."

# Run the program
run: $(TARGET)
	./$(TARGET)

# Help target
help:
	@echo "Available targets:"
	@echo "  make          - Build the program"
	@echo "  make clean    - Remove object files and executable"
	@echo "  make clean-all - Remove all files including data files"
	@echo "  make run      - Build and run the program"
	@echo "  make help     - Show this help message"

.PHONY: all clean clean-all run help

