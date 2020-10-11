#include <iostream>
#include <fstream>

#include <topology/persistence-diagram.h>

#include <boost/program_options.hpp>
namespace po = boost::program_options;

typedef PersistenceDiagram<>                    PDgm;
typedef PDgm::Point                             Point;


void    read_diagram(const std::string& filename, PDgm& dgm);
void    process_program_options(int argc, char* argv[], std::string& filename1, std::string& filename2, double& wasserPower);


int main(int argc, char* argv[])
{
    std::string     filename1, filename2;
    double wasserPower;
    process_program_options(argc, argv, filename1, filename2, wasserPower);

    PDgm dgm1, dgm2;
    read_diagram(filename1, dgm1);
    read_diagram(filename2, dgm2);

    std::cout << pow(wasserstein_distance(dgm1, dgm2, wasserPower), 1.0 / wasserPower) << std::endl;
}


void    read_diagram(const std::string& filename, PDgm& dgm)
{
    std::ifstream in(filename.c_str());
    double birth, death;
    while(in)
    {
        in >> birth >> death;
        //std::cout << "birth: " << birth << ", death: " << death << std::endl;
        if (in)
            dgm.push_back(Point(birth, death));
    }
}

void    process_program_options(int     argc, char* argv[], std::string& filename1, std::string& filename2, double& wasserPower)
{
    po::options_description hidden("Hidden options");
    hidden.add_options()
        ("input-file1",  po::value<std::string>(&filename1), "The first collection of persistence diagrams")
        ("input-file2",  po::value<std::string>(&filename2), "The second collection of persistence diagrams")
        ("wasser-power",  po::value<double>(&wasserPower), "The power of Wasserstein distance");

    po::positional_options_description p;
    p.add("input-file1", 1);
    p.add("input-file2", 1);
    p.add("wasser-power", 1);
    
    po::options_description all; all.add(hidden);

    po::variables_map vm;
    po::store(po::command_line_parser(argc, argv).
                  options(all).positional(p).run(), vm);
    po::notify(vm);

    if (!vm.count("input-file1") || !vm.count("input-file2"))
    { 
        std::cout << "Usage: " << argv[0] << " input-file1 input-file2" << std::endl;
        std::abort();
    }
    if (!vm.count("wasser-power")) 
    {
        // use L2 by default
        wasserPower = 2;
    }
}