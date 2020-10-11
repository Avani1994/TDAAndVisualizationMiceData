/**
 * Author: Dmitriy Morozov
 * Department of Computer Science, Duke University, 2006
 * 
 * Modified by Vanessa Robins August 2017 to use
 * Delaunay triangulations built with periodic boundary conditions
 *
 */

#ifndef __ALPHASHAPES3D_H__
#define __ALPHASHAPES3D_H__

#include <CGAL/Exact_predicates_exact_constructions_kernel.h>
// #include <CGAL/Delaunay_triangulation_3.h>
// VR: replaced with
#include <CGAL/Periodic_3_Delaunay_triangulation_traits_3.h>
#include <CGAL/Periodic_3_Delaunay_triangulation_3.h>


#include <topology/simplex.h>
#include <utilities/types.h>

#include <vector>
#include <set>
#include <iostream>

struct K: CGAL::Exact_predicates_exact_constructions_kernel {};

//typedef CGAL::Delaunay_triangulation_3<K>           Delaunay3D;
// VR: replaced with
typedef CGAL::Periodic_3_Delaunay_triangulation_traits_3<K> GT;
typedef CGAL::Periodic_3_Delaunay_triangulation_3<GT>   Delaunay3D;

typedef Delaunay3D::Point                           Point;
typedef Delaunay3D::Offset                          Offset;
//typedef Delaunay3D::Periodic_point                  Periodic_point;
typedef Delaunay3D::Vertex_handle                   Vertex_handle;
typedef Delaunay3D::Cell_handle                     Cell_handle;
typedef K::FT                                       RealValue;

typedef Delaunay3D::Vertex_iterator         Vertex_iterator;
typedef Delaunay3D::Edge_iterator           Edge_iterator;
typedef Delaunay3D::Facet_iterator          Facet_iterator;
typedef Delaunay3D::Cell_iterator           Cell_iterator;
typedef Delaunay3D::Facet_circulator        Facet_circulator;


class AlphaSimplex3D: public Simplex<Vertex_handle>
{
	public:
		typedef		Simplex<Vertex_handle>					            Parent;
		typedef 	std::set<AlphaSimplex3D, Parent::VertexComparison>  SimplexSet;
		typedef		Parent::VertexContainer								VertexSet;

    public:
									AlphaSimplex3D()					{}
									AlphaSimplex3D(const Parent& p): 
											Parent(p) 					{}
									AlphaSimplex3D(const AlphaSimplex3D& s): 
											Parent(s) 					{ attached_ = s.attached_; alpha_ = s.alpha_; }
	    							AlphaSimplex3D(const Delaunay3D::Vertex& v);
		
								    AlphaSimplex3D(const Delaunay3D::Edge& e);
								    AlphaSimplex3D(const Delaunay3D::Edge& e, const SimplexSet& simplices, const Delaunay3D& Dt, Facet_circulator facet_bg, const RealValue r);
		
								    AlphaSimplex3D(const Delaunay3D::Facet& f);
								    AlphaSimplex3D(const Delaunay3D::Facet& f, const SimplexSet& simplices, const Delaunay3D& Dt, const RealValue r);
	    
									AlphaSimplex3D(const Delaunay3D::Cell& c);
                                    AlphaSimplex3D(const Delaunay3D::Cell& c, const RealValue r);
	    
		RealType					value() const						{ return CGAL::to_double(alpha_); }
		RealValue					alpha() const						{ return alpha_; }
		bool						attached() const					{ return attached_; }

		// Ordering
		struct AlphaOrder
		{ bool operator()(const AlphaSimplex3D& first, const AlphaSimplex3D& second) const; };
	
        struct AlphaValueEvaluator
        { 
            typedef                 AlphaSimplex3D                                  first_argument_type;
            typedef                 RealType                                        result_type;

            RealType                operator()(const AlphaSimplex3D& s) const       { return s.value(); }
        };

		std::ostream& 				operator<<(std::ostream& out) const;
		
	private:
		RealValue 					alpha_;
		bool 						attached_;
};

void 				fill_simplex_set(const Delaunay3D& Dt, AlphaSimplex3D::SimplexSet& simplices);
template<class Filtration>
void 				fill_complex(const Delaunay3D& Dt,     Filtration& filtration);

std::ostream& 		operator<<(std::ostream& out, const AlphaSimplex3D& s)	{ return s.operator<<(out); }

#include "alphashapes3d-periodic.hpp"

#endif // __ALPHASHAPES3D_H__
