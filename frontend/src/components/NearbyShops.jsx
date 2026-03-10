import React, { useState } from "react";
import { Store, MapPin, Phone, Star, ArrowUpRight } from "lucide-react";
import { useTranslation } from "react-i18next";

const NearbyShops = ({ cropName }) => {
  const { t } = useTranslation();
  
  // Note: in a real application, this would fetch from a backend API using the user's geolocation.
  // For the business model demonstration, we'll provide mock top-rated local shops.
  const shops = [
    {
      id: 1,
      name: "Kisan Agro Center",
      distance: "2.4 km away",
      rating: 4.8,
      reviews: 124,
      specialty: "Organic Fertilizers & Seeds",
      phone: "+91 98765 43210",
      inStock: true
    },
    {
      id: 2,
      name: "Green Valley Farm Supplies",
      distance: "3.8 km away",
      rating: 4.6,
      reviews: 89,
      specialty: "Pesticides & Farming Tools",
      phone: "+91 87654 32109",
      inStock: true
    },
    {
      id: 3,
      name: "Shree Krishi Seva Kendra",
      distance: "5.1 km away",
      rating: 4.9,
      reviews: 210,
      specialty: "All Crop Solutions & Drip Irrigation",
      phone: "+91 76543 21098",
      inStock: true
    }
  ];

  return (
    <div className="bg-white rounded-2xl p-6 border border-emerald-100 shadow-sm mt-6">
      <div className="flex items-center justify-between mb-6 border-b pb-4">
        <div>
          <h3 className="text-2xl font-bold text-emerald-900 flex items-center gap-2">
            <Store className="w-6 h-6 text-emerald-600" />
            Recommended Local Shops
          </h3>
          <p className="text-emerald-700/70 text-sm mt-1">
            Verified sellers with treatments for {cropName || "your crops"} in stock
          </p>
        </div>
        <button className="text-emerald-600 hover:text-emerald-800 text-sm font-bold flex items-center gap-1 transition-colors">
          View on Map <ArrowUpRight className="w-4 h-4" />
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {shops.map((shop) => (
          <div key={shop.id} className="border border-gray-100 rounded-xl p-4 hover:border-emerald-300 hover:shadow-md transition-all group bg-gray-50/50 hover:bg-white">
            <div className="flex justify-between items-start mb-2">
              <h4 className="font-bold text-gray-900 group-hover:text-emerald-700 transition-colors">
                {shop.name}
              </h4>
              <div className="flex items-center gap-1 text-amber-500 text-xs font-bold bg-amber-50 px-2 py-0.5 rounded-full">
                <Star className="w-3 h-3 fill-current" /> {shop.rating}
              </div>
            </div>
            
            <div className="space-y-2 mt-3 text-sm text-gray-600">
              <p className="flex items-center gap-2">
                <MapPin className="w-4 h-4 text-gray-400" /> 
                {shop.distance}
              </p>
              <p className="flex items-center gap-2">
                <Store className="w-4 h-4 text-emerald-500" /> 
                <span className="text-emerald-700 font-medium text-xs">{shop.specialty}</span>
              </p>
            </div>

            <div className="mt-4 pt-4 border-t border-gray-100 flex items-center justify-between">
              <a href={`tel:${shop.phone}`} className="flex items-center gap-1.5 text-sm font-bold text-blue-600 hover:text-blue-800">
                <Phone className="w-4 h-4" /> Call Now
              </a>
              {shop.inStock && (
                <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-100">
                  Recommended items in stock
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NearbyShops;
